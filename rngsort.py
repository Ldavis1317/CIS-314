import random
import secrets
from collections import Counter

random_list = [] # Creates empty list
x = 0 
while x < 100:
    random_list.append(random.randrange(1,65535)) # Append 100 random numbers to the list in the range of 1,16
    x+=1

print(random_list)

secrets_list = []
y = 0
while y < 100:
    secrets_list.append(secrets.choice(range(1,65535))) # Append 100 random numbers using the secrets module
    y+=1

print(secrets_list)

random_count = Counter(random_list) # Creates the counter to find the number of unique numbers 
secrets_count = Counter(secrets_list)

print(random_count)
print(secrets_count)

#-------------------------------------
## For 1-16
## After running multiple times both methods seem to randomize the number effectively
## Neither one has an abundance of one number or another
#--------------------------------------
## For 1-65535
## Using this wide range of numbers didn't affect either method
## It just made it so every number was only used once
# -------------------------------------


