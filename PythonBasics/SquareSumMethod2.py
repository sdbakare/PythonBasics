# sum of square of first N natural number = (N * (N+1)*(2*N+1))/6
# For example
# For N = 4, Sum = (4*(4+1)* (2*4+1))/6
#                 = (4 * 5 * 9)/6
#                 = 180/6
#                 = 30
# For N = 5, Sum = (5*(5+1)*(2*5+1))/6
#                 =(5*6*11)/6
#                 = 55


def SquareSum(n):
    return (n*(n+1) * (2*n+1))// 6



#Drivers code
n = 4
print(SquareSum(n))