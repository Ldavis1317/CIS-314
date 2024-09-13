import random

golfclubstuple = ("Driver", "3 Wood", "5 Wood", "4 iron", "5 iron", "6 iron", "7 iron", "8 iron", "Sand Wedge", "Putter")
golfclubslist = ["Putter", "Sand Wedge", "8 iron", "7 iron", "6 iron", "5 iron", "4 iron", "5 Wood", "3 Wood", "Driver"]

# Print elements at index 2
print(golfclubstuple[2])
print(golfclubslist[2])

# Shuffle the list (temporary for display purposes only)
shuffled_golfclubslist = golfclubslist[:]  # Create a copy of the original list
random.shuffle(shuffled_golfclubslist)
print("Shuffled List:", shuffled_golfclubslist)  # Print shuffled list

# Shuffle the tuple (by converting it to a list, shuffling, and converting back to a tuple)
shuffled_golfclubstuple = list(golfclubstuple)  # Create a copy of the tuple as a list
random.shuffle(shuffled_golfclubstuple)         # Shuffle the copy
shuffled_golfclubstuple = tuple(shuffled_golfclubstuple)  # Convert back to tuple
print("Shuffled Tuple:", shuffled_golfclubstuple)  # Print shuffled tuple

# Now continue using the original list and tuple without further shuffling
golfclubslist.append("Lob Wedge")
print("List with new Element:", golfclubslist)

# Add a new element to the tuple (convert to list, append, and convert back)
golfclubstuple = list(golfclubstuple)  # Convert tuple to list
golfclubstuple.append("Lob Wedge")     # Append new element
golfclubstuple = tuple(golfclubstuple)  # Convert back to tuple
print("Tuple with new element:", golfclubstuple)

# Remove the first element from the list
golfclubslist.pop(0)
print("List without First Element:", golfclubslist)

# Print tuple without the first element
print("Tuple without First Element:", golfclubstuple[1:])
