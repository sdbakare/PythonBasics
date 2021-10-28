# Performance Analysis – Naive vs len() vs length_hint()

from operator import length_hint
import time


# initializing list

test_list = [1, 4, 5, 7, 8]
print("the list is :", str(test_list))

# Finding length of list
# using loop
# Initializing counter

start_time_naive = time.time()
counter = 0
for j in range(100000000):
    for i in test_list:
        counter = counter + 1

end_time_naive = str(time.time() - start_time_naive)

# Finding length of list
# using len()

start_time_len = time.time()
list_len = len(test_list)
for i in range (100000000):
    len(test_list)
end_time_len = str(time.time() - start_time_len)

# Finding length of list
# using length_hint

start_time_length_hint = time.time()
list_length_hint = length_hint(test_list)
for i in range (100000000):
    length_hint(test_list)
end_time_length_hint = str(time.time() - start_time_length_hint)

print("Time take by naive method is : ", end_time_naive)
print("Time take by len method is :", end_time_len)
print("Time take by length_hint method is :", end_time_length_hint)
