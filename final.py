import tkinter as tk
from tkinter import messagebox
import re
import random
import string

password_file = "Password_file.txt"  # Variable storing a text file where weak passwords will be written

def password_strength(password):
    strength = 0  # Initialize the password strength
    feedback = []  # Empty list to store feedback

    if len(password) >= 8:  # Check if password is 8 characters long
        strength += 1  # If true, increase strength by 1
    else:
        feedback.append("Password should be at least 8 characters long.")  # If not, return this

    if re.search(r'[a-z]', password):  # Uses regular expressions to check if password includes a lowercase letter
        strength += 1
    else:
        feedback.append("Password needs at least one lowercase letter.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password needs at least one uppercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password needs at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password needs at least one special character.")

    if not re.search(r'(password|123|admin|forget)', password, re.IGNORECASE):  # Ignore case recognizes patterns no matter the capitalization
        strength += 1
    else:
        feedback.append("Avoid using common passwords like password, 123, admin, and forget")

    if strength >= 6:  # Determine overall strength of password
        return "Strong Password!", feedback

    elif strength >= 4:  # Determine if it's moderate
        return "Moderate password, could use some strengthening.", feedback
    else:  # Determine if it's weak 
        return "Weak password, needs improvement.", feedback


def save_feedback(feedback):
    # Append feedback to password file
    with open(password_file, "a") as f:  # Open with the append mode
        f.write("Password Feedback: " + ", ".join(feedback) + "\n")  # Join feedback with a comma


def generate_recommendations(feedback, user_input):
    # Modify the user's input to meet the strength criteria
    recommended_password = list(user_input)

   # Ensure the recommended password meets all criteria
    if "Password should be at least 8 characters long." in feedback:
        while len(recommended_password) < 8:  # Ensure the password is at least 8 characters long
            recommended_password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
    
    # If password is missing a lowercase add lowercase letter in the suggested password
    if "Password needs at least one lowercase letter." in feedback:
        if not any(char for char in recommended_password if char in string.ascii_lowercase):
            recommended_password.append(random.choice(string.ascii_lowercase))
    # If password is missing a uppercase add uppercase ketter in the suggested password
    if "Password needs at least one uppercase letter." in feedback:
        if not any(char for char in recommended_password if char in string.ascii_uppercase):
            recommended_password.append(random.choice(string.ascii_uppercase))

    if "Password needs at least one digit." in feedback:
        if not any(char for char in recommended_password if char in string.digits):
            recommended_password.append(random.choice(string.digits))

    if "Password needs at least one special character." in feedback:
        if not any(char for char in recommended_password if char in string.punctuation):
            recommended_password.append(random.choice(string.punctuation))

    
    if "Avoid using common passwords like password, 123, admin, and forget" in feedback:
        recommended_password = [char for char in recommended_password if char.lower() not in ["password", "123", "admin", "forget"]]
        while len(recommended_password) < 12:
            recommended_password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    
    # Join shuffled password back into a string
    return ''.join(recommended_password)

def check_password():
    user_input = password_entry.get() # Get user input
    result, suggestions = password_strength(user_input) # Evaluate password strength and get suggestions

    result_label.config(text=result) # Update the result label

    if suggestions:
        feedback_text.set("\n".join(suggestions)) # Join suggestions with newlines for display
    else:
        feedback_text.set("") # Clear suggestions if none exist

    if result.startswith("Weak"): # If the password is weak, save feedback and generate a recommended strong password
        save_feedback(suggestions)
        recommended_password = generate_recommendations(suggestions, user_input) # Generate a stronger password
        recommendation_label.config(text=f"Recommended Password: {recommended_password}") # Update the recommendation label
    else:
        recommendation_label.config(text="")  # Clear the recommendation label for non-weak passwords

root = tk.Tk()
root.title("Password Strength Checker") # Set the title 


tk.Label(root, text="Enter your password:").pack(pady=5) # Create and pack the label for password 
password_entry = tk.Entry(root, width=30) # Input field for user to type password
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=check_password) # Button triggers the check_password function
check_button.pack(pady=10) 

# Create and pack the label to display password strength results
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=5)

tk.Label(root, text="Suggestions:").pack(pady=5) # Create and pack the label for improvement suggestions
feedback_text = tk.StringVar() # Variable to dynamically update suggestions
feedback_label = tk.Label(root, textvariable=feedback_text, fg="red", justify="left")
feedback_label.pack(pady=5)

recommendation_label = tk.Label(root, text="", fg="green", wraplength=300) # Shows a stronger recommended password if needed
recommendation_label.pack(pady=10)

# Run the application
root.mainloop()