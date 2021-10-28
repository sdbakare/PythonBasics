#Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.
# n! = n * (n-1) * (n-2) * (n-3)......*1

# Example1  4! = 4*3*2*1 = 24
# Example2  6! = 6*5*4*3*2*1 = 720
# Python 3 program to find
# factorial of given number

def factorial(n):
# single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n-1);
# Driver Code

num = 6

print("factorial of ", num ,"is", factorial(num))