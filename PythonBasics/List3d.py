#Demonstrating finding length of list using len() and length_hint()
# output required :
# The list is : [1, 4, 5, 7, 8]
# Length of list using len() is : 5
# Length of list using length_hint() is : 5

from operator import length_hint

test_list = [1, 4, 5, 7, 8]

print ("the list is :", str(test_list))

List_Length = len (test_list)
# using length_hint()
List_Length_hint = length_hint(test_list)

print("Length of the list using len() is :", str(List_Length))
print("Length of the list using length_hint() is :", str(List_Length_hint))
