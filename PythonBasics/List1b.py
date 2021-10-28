# python3 program to swap first and last element of a list

# swap function

def swapList(newList):

    newList[0], newList[-1] = newList[-1], newList[0]
    return newList


# Drivers code

newList = [12, 35,9,56,24]
print(swapList(newList))