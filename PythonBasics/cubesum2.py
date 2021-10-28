# using direct mathematical formula which is (n ( n + 1 ) / 2) ^ 2
# A formula based Python program to find sum
# of series with cubes of first n natural
# numbers

# Returns the sum of series

def sumofSeries(n):
    x = (n * (n+1)/2)
    return int(x * x)

# Drivers function

n = 5
print ("cube sum of given number is ", sumofSeries(n))

