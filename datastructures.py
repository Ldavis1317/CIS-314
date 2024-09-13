import random

golfclubstuple = ("Driver","3 Wood","5 Wood", "4 iron", "5 iron", "6 iron","7 iron", "8 iron", "Sand Wedge", "Putter")
golfclubslist = ["Putter", "Sand Wedge", "8 iron","7 iron" , "6 iron", "5 iron", "4 iron","5 Wood","3 Wood", "Driver"]

print(golfclubstuple[2])
print(golfclubslist[2])

randomlist = golfclubslist[:] # Creates a copy of the list
random.shuffle(randomlist)
print("Shuffled List:", randomlist)

# Tuples are immutable so I had to switch the tuple to a list in able to randomize the tuple
randomtuple = list(golfclubstuple) # Creates a copy of the tuple
random.shuffle(randomtuple)
golfclubstuple = tuple(golfclubstuple)
print("Shuffled Tuple:", randomtuple)


golfclubslist.append("Lob Wedge")

print("List with new Element:", golfclubslist)

# Same case as the one above, tuples are immutable so I had to switch tuple to a list to be able to add a new element
golfclubstuple = list(golfclubstuple)

golfclubstuple.append("Lob Wedge")

# Switch back to tuple
golfclubstuple = tuple(golfclubstuple)

print("Tuple with new element:", golfclubstuple)

golfclubslist.pop(0)
print("List without First Element", golfclubslist)

# To print a tuple without the first element I had to splice the Tuple to print without the first
# element since you can't remove anything from a tuple
print("Tuple without First Element", golfclubstuple[1:])

golfclubslist.pop(6)
print("List without 5 wood:", golfclubslist)

# Switch tuple to list to be able to remove the same element of the list 
golfclubstuple = list(golfclubstuple)
golfclubstuple.pop(1)
golfclubstuple = tuple(golfclubstuple)

print("Tuple without 5 wood:", golfclubstuple)





