#One line Solution (Using Ternary operator):

# Python 3 program to find
# factorial of given number

def factorial(n):
# single line to find factorial
    return 1 if (n == 0 or n == 1) else n * factorial(n-1)

# Driver Code
num = 5
print("factorial of ", num, "is",factorial(num))
