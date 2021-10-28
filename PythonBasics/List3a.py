#Demonstrating finding length of list using Naive Method
# Python code to demonstrate length of list using naive method

# initializing list

test_list = [1, 4, 5, 7, 8]
#printing test list

print("the list is"  +  str(test_list))

# finding length of the list using loop
# initializing counter
counter = 0
for i in test_list:
        # incrementing counter
        counter = counter +1

print("Length of list using naive method is : "  + str(counter))
