import re

password_file = "password_file.txt"

def password_strength(password):
    strength = 0
    feedback = []

    if len(password) >=8:
        strength +=1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r'[a-z]', password):
        strength+=1
    else: 
        feedback.append("Password needs at least one lowercase letter.")
    
    if re.search(r'[A-Z]', password):
        strength+=1
    else:
        feedback.append("Passowrd needs at least one uppercase letter.")
    
    if re.search(r'[0-9]', password):
        strength+=1
    else:
        feedback.append("Password needs at least one digit.")
    
    if re.search(r'[]',password):
        strength+=1
    else:
        feedback.append("Password needs at least one special character.")