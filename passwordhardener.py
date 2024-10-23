import re

password_file = "password_file.txt" # variable storing a text file where weak passwords will be written

def password_strength(password):
    strength = 0 # intialize the password strength
    feedback = [] # empty list to store feedback


    if len(password) >=8: # check if password is 8 characters long
        strength +=1 # if true increase strength by 1
    else:
        feedback.append("Password should be at least 8 characters long.")  # if not return this
    
    if re.search(r'[a-z]', password): # uses regular expressions to check if password includes a lowercase letter
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