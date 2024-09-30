import random
import secrets
from collections import Counter
import time

random_list = [] # Creates empty list
x = 0 
while x < 100:
    random_list.append(random.randrange(1,17)) # Append 100 random numbers to the list in the range of 1,16
    x+=1

print(random_list)

secrets_list = []
y = 0
while y < 100:
    secrets_list.append(secrets.choice(range(1,17))) # Append 100 random numbers using the secrets module
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

def bubble_sort(arr):
    n = len(arr) 
    for i in range(n):
        swapped = False # swapped variable set to false at the beginning of each loop iteration
        for j in range(n-i-1):
           if arr[j] > arr[j+1]: # check if current element is greater than next element
               arr[j], arr[j+1] = arr[j+1], arr[j] # swaps the smaller elements with the larger ones
               swapped = True
        if not swapped:
            break
    return arr


random_list2 = [] # Creates empty list
x = 0 
while x < 100:
    random_list2.append(random.randrange(1,17)) # Append 100 random numbers to the list in the range of 1,16
    x+=1

normal_sort2 = random_list2.copy()

print("Unsorted List:",random_list2)

start_time = time.time()

bubble_sort(random_list2)

end_time = time.time()

print("Sorted List:",random_list2)
print("Time taken to sort the 100 element list between 1-16: {:.10f} seconds".format(end_time - start_time)) # Prints the time it takes to sort the list with 10 decimal places


random_list3 = [] # Creates empty list
x = 0 
while x < 100:
    random_list3.append(random.randrange(1,65535)) # Append 100 random numbers to the list in the range of 1,65535
    x+=1

normal_sort3 = random_list3.copy()
start_time = time.time()

bubble_sort(random_list3)

end_time = time.time()

#print("Sorted List:",random_list3)

print("Time taken to sort the 100 element list between 1-65535: {:.10f} seconds".format(end_time - start_time))

random_list4 = [] # Creates empty list
x = 0 
while x < 500:
    random_list4.append(random.randrange(1,65535)) # Append 500 random numbers to the list in the range of 1,65535
    x+=1

normal_sort4 = random_list4.copy()
start_time = time.time()

bubble_sort(random_list4)

end_time = time.time()

#print("Sorted List:",random_list4)

print("Time taken to sort the 500 element list between 1-65535: {:.10f} seconds".format(end_time - start_time))


start_time = time.time()

normal_sort2.sort()

end_time = time.time()

print("Time taken to sort 100 element list between 1-16 using sort(): {:.10f} seconds".format(end_time - start_time))

start_time = time.time()

normal_sort3.sort()

end_time = time.time()

print("Time taken to sort 100 element list between 1-65535 using sort(): {:.10f} seconds".format(end_time - start_time))

start_time = time.time()

normal_sort4.sort()

end_time = time.time()

print("Time taken to sort 500 element list between 1-65535 using sort(): {:.10f} seconds".format(end_time - start_time))

#-------------------------------------------------------
## The 100 element list was hardly affected at all when the range of numbers were increased
## When the number of elements was increased from 100 to 500 there was a substantial increase in the execution time
## The Bubble sort seems to be more efficient for the 100 element list no matter the range size compared to .sort()
## .sort() was a little faster when executing the larger data sets like the 500 element list then the bubble sort function I created
#--------------------------------------------------------