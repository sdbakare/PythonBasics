# Python3 program to swap first and last element of a list
# Swap function

def swapList(newList):
    start, *middle, end = newList
    newList = [end, *middle, start]

    return newList

#Driver's code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

