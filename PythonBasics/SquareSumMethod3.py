# Avoiding overflow, For large n, the value of (n * (n + 1) * (2 * n + 1)) would overflow.
# We can avoid overflow up to some extent using the fact that n*(n+1) must be divisible by 2.

# Python Program to find sum of square of first
# n natural numbers. This program avoids
# overflow upto some extent for large value
# of n.y

def squaresum(n):
    return int ((n * (n+1) / 2) * (2 * n + 1) / 3)


# Drivers code

n = 5

print (squaresum(n))