#Approach #5: Swap the first and last elements is to use the inbuilt function list.pop().
# Pop the first element and store it in a variable. Similarly, pop the last element and store it in another variable.
# Now insert the two popped element at each other’s original position.


def swapList(List):

    first = List.pop(0)

    last = List.pop(-1)
    
    List.insert(0, last)
    List.append(first)

    return List

# Driver's code
List = [12, 35, 9, 56, 24]
print(swapList(List))