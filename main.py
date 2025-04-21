import streamlit as st

def check_password_strength(password):
    """Evaluate the strength of a password based on various criteria."""
    
    score = 0
    feedback = []
    
    # Check for empty password
    if not password:
        return 0, "Empty", ["Please enter a password"]
    
    # Criteria checks
    length_ok = len(password) >= 8
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_chars = "!@#$%^&*"
    has_special = any(c in special_chars for c in password)
    has_space = ' ' in password
    
    # Calculate score
    if length_ok:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    if has_lower:
        score += 1
    else:
        feedback.append("Password should contain lowercase letters.")
        
    if has_upper:
        score += 1
    else:
        feedback.append("Password should contain uppercase letters.")
        
    if has_digit:
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")
        
    if has_special:
        score += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*).")
    
    # Additional checks
    if has_space:
        feedback.append("⚠️ Password contains spaces (not recommended).")
    
    if len(password) > 64:
        feedback.append("⚠️ Password is very long (may be hard to remember).")
    
    # Check for common patterns
    common_patterns = ['123', 'abc', 'qwerty', 'password']
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("⚠️ Password contains common patterns (easy to guess).")
    
    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return score, strength, feedback

def main():
    st.title("🔒 Password Strength Meter")
    st.write("Evaluate your password security based on multiple criteria")
    
    password = st.text_input("Enter your password:", type="password")
    
    if password is not None:
        score, strength, feedback = check_password_strength(password)
        
        # Display results with color coding
        if strength == "Strong":
            st.success(f"Password Strength: {strength} (Score: {score}/5)")
            st.balloons()
        elif strength == "Moderate":
            st.warning(f"Password Strength: {strength} (Score: {score}/5)")
        elif strength == "Weak":
            st.error(f"Password Strength: {strength} (Score: {score}/5)")
        else:  # Empty
            st.info("Please enter a password to evaluate")
        
        # Show feedback if not strong
        if strength != "Strong" and strength != "Empty":
            st.subheader("Recommendations to improve:")
            for item in feedback:
                st.write(f"- {item}")
        
        # Visual strength meter
        st.progress(score/5)

if __name__ == "__main__":
    main()