# creating an array in the function to find the nth number in fibonacci series. [0, 1, 1, ...]

#ip= number 9
#op= 0,1,1,2,3,5,8,13,21
import pdb
pdb.set_trace()
def fibonacci(n):
    pdb.set_trace()
    if n <= 0:
        print("Incorrect Output")
    data = [0,1]
    if n > 2:
        for i in range (2, n):
            print("i re i" , i)
            data.append(data[i - 1] + data[i - 2])  # operation on indexing here in data, + getting values with index
            print("data is = " , data)
        return data[n-1]


# Drivers code
print(fibonacci(9))
a = fibonacci(9)
print(a)
