# Efficient Python program to find sum of cubes
# of first n natural numbers that avoids
# overflow if result is going to be within limits.

# Returns the sum of series

def sumofSeries(n):
    x = 0
    if n % 2 == 0:
        x = (n/2) * (n+1)

    else:
        x = ((n+1)/2) * n

    return int (x * x)

# Drivers function
n = 5
print("the cubesum for given n number is", sumofSeries(n))


