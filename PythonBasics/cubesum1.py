# Simple Python program to find sum of series
# with cubes of first n natural numbers

# Returns the sum of series

def sumCube(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i*i
    return sum


# Drivers code
n = 5
print ("the cubes sum of given number is", sumCube(n))

