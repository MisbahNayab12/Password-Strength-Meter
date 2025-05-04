import streamlit as st
import string

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("❗ Password should be at least 8 characters long.")

    if any(c.islower() for c in password):
        strength += 1
    else:
        remarks.append("❗ Add lowercase letters (a-z).")

    if any(c.isupper() for c in password):
        strength += 1
    else:
        remarks.append("❗ Add uppercase letters (A-Z).")

    if any(c.isdigit() for c in password):
        strength += 1
    else:
        remarks.append("❗ Add numbers (0-9).")

    if any(c in string.punctuation for c in password):
        strength += 1
    else:
        remarks.append("❗ Add special characters (!@# etc).")

    if strength == 5:
        return "✅ Strong Password", remarks
    elif strength >= 3:
        return "⚠️ Medium Strength Password", remarks
    else:
        return "❌ Weak Password", remarks

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    result, remarks = check_password_strength(password)
    st.subheader(result)

    if remarks:
        st.write("### Suggestions to improve:")
        for tip in remarks:
            st.write("- " + tip)

