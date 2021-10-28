# swap Using Inbuilt list.pop() function
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

def swapPositions(list, pos1, pos2):

    # popping
    first = list.pop(pos1)
    second = list.pop(pos2-1)



    # swapping
    list.insert(pos1, second)
    list.insert(pos2, first)

    return list

# Drivers code

list = [23, 65, 19, 90]
pos1 , pos2 = 1 , 3

print(swapPositions(list, pos1-1, pos2-1))
