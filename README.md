# Password Strength Evaluator

## Description
This program will prompt the user to enter in a password. After the user enters their password it will be either validated or recommendations will be given to the user based on how strong their password is. If the password is considerated weak, the program will give a recomended password by adding all of the missing criteria that is needed for a strong password to the users intial password. The goal of this program is to have the user enter in their password and if their password is not already strong it will be after running it through our evaluator. 

## Roadblocks
Some of the struggles we ran into doing this final project was mostly implementing ascii in the generating recomended function. It took awhile trying to get the if statements working because they would not function properly using char.isupper and char.islower. We then had to use compact for loops inside of the any function which allowed the code to run properly. 