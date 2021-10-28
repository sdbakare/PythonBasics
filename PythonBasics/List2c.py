# Using tuple variable
# Store the element at pos1 and pos2 as a pair in a tuple variable, say get.
# Unpack those elements with pos2 and pos1 positions in that list.
# Now, both the positions in that list are swapped.
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

def swapPositions(list, pos1, pos2):

    get = list[pos1], list[pos2]

    # unpacking
    list[pos2], list[pos1] = get

    return list

# Drivers code

list = [23, 65, 19, 90]
pos1, pos2 = 1 ,3

print(swapPositions(list, pos1-1, pos2-1))
