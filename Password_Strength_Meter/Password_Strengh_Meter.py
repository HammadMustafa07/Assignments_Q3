import streamlit as st 
import re

# Page setup
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
st.title("🔒 Password Strength Meter")

st.markdown("""
## Welcome to the Ultimate Password Strength Meter!
Use this simple tool to check the strength of your **password**.
""")

# Input from user
password = st.text_input("Enter your Password", type="password")

feedback = []
score = 0

# Only check if password is entered
if password:
    # Rule 1: Minimum length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    # Rule 2: Upper and lower case
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both lowercase and uppercase letters.")

    # Rule 3: At least one number
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one number.")

    # Rule 4: At least one special character
    if re.search(r'[@#$%&*+]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (@#$%&*+).")

    # Visual strength meter (progress bar)
    st.markdown("### 📊 Password Strength:")
    st.progress(score / 4)  # Convert to 0.0 - 1.0 range

    # Colorful message based on strength
    if score == 4:
        st.success("✅ Your password is strong!")
    elif score == 3:
        st.warning("⚠️ Your password is moderately strong. Try adding more variety!")
    elif score <= 2:
        st.error("🔴 Your password is weak. Improve the above areas.")

    # Suggestions for improvement
    if feedback:
        st.markdown("### 🔧 Suggestions for Improvement:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")

















# # Importing required libraries
# import streamlit as st       # Streamlit is used to build the web interface
# import re                    # re (regular expressions) is used to analyze the password pattern

# # Setting up the page title and icon
# st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

# # Main title displayed on the web app
# st.title("🔒 Password Strength Meter")

# # Some instructions for users written in markdown
# st.markdown("""
# ## Welcome to the Ultimate Password Strength Meter!
# Use this simple tool to check the strength of your **password**.
# """)

# # Input field for the user to enter their password (it hides the text)
# password = st.text_input("Enter your Password", type="password")

# # A list to store suggestions and feedback for the user
# feedback = []

# # A variable to keep track of the password's strength score
# score = 0

# # If the user has entered a password
# if password:
    
#     # Check 1: Is the password at least 8 characters long?
#     if len(password) >= 8:
#         score += 1  # Add 1 point if condition is true
#     else:
#         feedback.append("❌ Password must be at least 8 characters long.")

#     # Check 2: Does the password contain both uppercase and lowercase letters?
#     if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
#         score += 1
#     else:
#         feedback.append("❌ Password should contain both lowercase and uppercase letters.")

#     # Check 3: Does the password contain at least one number?
#     if re.search(r'\d', password):
#         score += 1
#     else:
#         feedback.append("❌ Password should contain at least one number.")

#     # Check 4: Does the password include at least one special character?
#     if re.search(r'[@#$%&*+]', password):
#         score += 1
#     else:
#         feedback.append("❌ Password should contain at least one special character (@#$%&*+).")

#     # Final feedback based on the total score
#     if score == 4:
#         feedback.append("✅ Your password is strong!")  # Best case
#     elif score == 3:
#         feedback.append("⚠️ Your password is moderately strong.")  # Almost strong
#         feedback.append("🛡️ You can make your password strong! 🔥🔑")
#     elif score <= 2:
#         feedback.append("🔴 Your password is weak.")  # Needs improvement

#     # Show all suggestions and feedback to the user
#     st.markdown("### 🔧 Suggestions for Improvement:")
#     for tip in feedback:
#         st.write(tip)

# else:
#     # If no password is entered yet
#     st.info("Please enter your password to get started.")




































































































# # import streamlit as st 
# # import re

# # st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

# # st.title("🔒 Password Strength Meter")

# # st.markdown("""
# #    ##Welcome to the Ultime Password Strength Meter!
# #    use this simple tool to checkl the strength of your **password**
# # """)

# # password = st.text_input("Enter your Password", type="password")

# # feedback = []

# # score = 0

# # if password:
# #     if len(password) >= 8:
# #         score += 1
# #     else:
# #         feedback.append("Password must be at least 8 characters long.")

# #     if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password)
# #         score += 1
# #     else:
# #         feedback.append("❌Password should contain both lower case and upper case letters")

# #     if re.search(r'\d' , password):
# #         score += 1
# #     else:
# #         feedback.append("��Password should contain at least one number")

# #     if re.search(r'[@#$%&*+]', password):
# #         score += 1
# #     else:
# #         feedback.append("��Password should contain at least one special character(@#$%&*+)")

# #     if score == 4:
# #         feedback.append("Your password is strong")
# #     elif score == 3:
# #         feedback.append("Your password is moderately strong")

# #     else score == 2:
# #         feedback.append("Your password is weak")

# #     if feedback:
# #         st.markdown("improvement suggestions")
# #         for tip in feedback:
# #             st.write(tip)

# # else:
# #     st.info("please enter your password to get started")