#python program to check if x is perfect square
import math

def isPerfectSquare(x):
    s = int (math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)

# A utility function to test above functions
for i in range (1,11):
    if (isFibonacci(i)== True):
        print(i, "is Fibonacci number")
    else:
        print(i, "is not a Fibonacci number")
