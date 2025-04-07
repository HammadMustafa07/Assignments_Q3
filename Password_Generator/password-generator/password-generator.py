import streamlit as st
import random 
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation  # add special characters (!, @ etc)

    return ''.join(random.choice(characters) for _ in range(length))

# Upgraded Title
st.title("🔐 Secure Password Generator")

# Slider with polished label
length = st.slider("🔧 Choose your password length", min_value=6, max_value=32, value=12)

# Enhanced checkboxes
use_digits = st.checkbox("🔢 Include numbers (0-9)")
use_special = st.checkbox("✨ Include special characters (!, @, #, etc)")

# Styled button
if st.button("🚀 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success("✅ Here’s your secure password:")
    st.code(password, language='')

# Divider with style
st.markdown("---")

# Credit line upgrade
st.caption("🧠 Created by Hammad Mustafa")









































































# import streamlit as st
# import random 
# import string

# def generate_password(length, use_digits, use_special):
#     characters = string.ascii_letters

#     if use_digits:
#         characters += string.digits

#     if use_special:
#         characters += string.punctuation  # add special characters (!, @ etc)\

#     return '' .join(random.choice(characters) for _ in range(length))

# st.title("Password Generator")

# length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

# use_digits = st.checkbox("Include Digits")

# use_special = st.checkbox("include special characters")

# if st.button("Generate Password"):
#     password = generate_password(length, use_digits, use_special)
#     st.write(f"Generated Password: `{password}`")

# st.write("------------------------------------------------------------")

# st.write("made By Hammad Mustafa")


    









































































# # def main():
# #     print("Hello from password-generator!")


# # if __name__ == "__main__":
# #     main()
