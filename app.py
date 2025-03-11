import streamlit as st

# Function to check password strength
def check_password_strength(password):
    """
    Evaluates the strength of a given password based on length, character variety, and complexity.
    """
    score = 0
    feedback = []
    
    # List of commonly used weak passwords
    common_passwords = {"password", "123456", "password123", "qwerty", "abc123", "letmein", "welcome", "admin", "12345678"}
    if password.lower() in common_passwords:
        return "🔴 Weak ❌", "This password is too common. Choose something more unique! 🚨"
    
    # Check password length
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("📏 Make your password at least 8 characters long.")
    
    # Check for mix of uppercase and lowercase letters
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 2
    else:
        feedback.append("🔠 Include both uppercase and lowercase letters.")
    
    # Check for at least one digit
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("🔢 Include at least one digit (0-9).")
    
    # Check for at least one special character
    if any(c in "!@#$%^&*" for c in password):
        score += 2
    else:
        feedback.append("🔣 Include at least one special character (!@#$%^&*).")
    
    # Determine password strength based on score
    if score >= 7:
        return "🟢 Strong ✅", "🎉 Great job! Your password is strong and secure! 🔒"
    elif score >= 4:
        return "🟡 Moderate ⚠️", "💡 Your password is decent but could be stronger. " + " ".join(feedback)
    else:
        return "🔴 Weak ❌", "⚠️ Your password is weak. " + " ".join(feedback)

# Streamlit UI
st.title("🔒 Password Strength Meter")
st.markdown("## 🔐 Secure your accounts with a strong password! 🛡️")
password = st.text_input("🔑 Enter Password:", type="password")

# Button to check password strength
if st.button("🚀 Check Strength"):
    if password:
        strength, message = check_password_strength(password)
        st.markdown(f"**📝 Strength:** {strength}")
        st.markdown(f"**📢 Feedback:** {message}")
    else:
        st.warning("⚠️ Please enter a password to check its strength! 🔍")