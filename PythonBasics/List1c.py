# Python3 program to swap first
# and last element of a list

def swapList(newList):
    get = newList[0],newList[-1]

    # unpacking
    newList[-1], newList[0] = get

    return newList

# Driver's code
newList = [12, 35,9,56,24]
print(swapList(newList))
