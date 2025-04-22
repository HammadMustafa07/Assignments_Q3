import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# === Constants ===
DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"  # Used for password hashing – should remain the same across sessions
LOCKOUT_DURATION = 60  # Lockout duration after too many failed login attempts (in seconds)

# === Initialize session state variables ===
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# === Helper Functions ===

def load_data():
    # Load existing user data from JSON file
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    # Save user data back to the JSON file
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def generate_key(passkey):
    # Create a secure encryption key using PBKDF2 and base64 encoding
    key = pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

def hash_password(password):
    # Hash a user's password for secure storage
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

def encrypt_text(text, key):
    # Encrypt user data with the given key
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()

def decrypt_text(encrypted_text, key):
    # Decrypt data using the provided key
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypted_text.encode()).decode()
    except:
        return None

# === Load data from storage ===
stored_data = load_data()

# === Navigation Menu ===
st.title("🔐 Secure Multi-User Data System")
menu = ["Home", "Register", "Login", "Store Data", "Retrieve Data"]
choice = st.sidebar.selectbox("Choose a section", menu)

# === Home Page ===
if choice == "Home":
    st.subheader("🏠 Welcome to Your Personal Vault")
    st.markdown("Easily encrypt and save your personal data securely. Each user has their own encrypted storage.")

# === Registration Page ===
elif choice == "Register":
    st.subheader("📝 Create a New Account")
    username = st.text_input("Enter a username")
    password = st.text_input("Enter a password", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning("⚠️ That username is already taken.")
            else:
                stored_data[username] = {
                    "password": hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("✅ Account created successfully!")
        else:
            st.error("Please fill in both fields.")

# === Login Page ===
elif choice == "Login":
    st.subheader("🔑 Sign In to Your Account")
    
    # Check if the user is currently locked out
    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"⏳ Too many failed attempts. Try again in {remaining} seconds.")
        st.stop()

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in stored_data and stored_data[username]["password"] == hash_password(password):
            st.session_state.authenticated_user = username
            st.session_state.failed_attempts = 0
            st.success(f"✅ Welcome back, {username}!")
        else:
            st.session_state.failed_attempts += 1
            remaining = 3 - st.session_state.failed_attempts
            st.error(f"❌ Incorrect username or password. Attempts remaining: {remaining}")

            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                st.error("🔒 You've been locked out for 60 seconds due to multiple failed attempts.")
                st.stop()

# === Store Encrypted Data ===
elif choice == "Store Data":
    if not st.session_state.authenticated_user:
        st.warning("🔒 Please log in to store your data.")
    else:
        st.subheader("📦 Save Encrypted Information")
        data = st.text_area("Type the data you want to encrypt and save")
        passkey = st.text_input("Choose an encryption passphrase", type="password")

        if st.button("Encrypt & Save"):
            if data and passkey:
                encrypted = encrypt_text(data, passkey)
                stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
                save_data(stored_data)
                st.success("✅ Your data has been securely encrypted and stored.")
            else:
                st.error("Please fill in all fields.")

# === Retrieve and Decrypt Data ===
elif choice == "Retrieve Data":
    if not st.session_state.authenticated_user:
        st.warning("🔒 You need to log in to view your stored data.")
    else:
        st.subheader("🔎 View & Decrypt Your Data")
        user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])

        if not user_data:
            st.info("ℹ️ You have no data stored yet.")
        else:
            st.write("🔐 Your Encrypted Entries:")
            for i, item in enumerate(user_data):
                st.code(item, language="text")

            encrypted_input = st.text_area("Paste an encrypted entry here to decrypt")
            passkey = st.text_input("Enter your passphrase to decrypt", type="password")

            if st.button("Decrypt"):
                result = decrypt_text(encrypted_input, passkey)
                if result:
                    st.success(f"✅ Here's your decrypted data: {result}")
                else:
                    st.error("❌ Decryption failed. Check your passphrase or the encrypted text.")
