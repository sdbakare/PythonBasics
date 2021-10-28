# Python Program for simple interest

# Simple interest formula is given by:
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

# EXAMPLE1:
# Input : P = 10000
#         R = 5
#         T = 5
# Output :2500
# We need to find simple interest on
# Rs. 10,000 at the rate of 5% for 5
# units of time.
#
# EXAMPLE2:
# Input : P = 3000
#         R = 7
#         T = 1
# Output :210



# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.



def simple_interest(p,t,r):
    print ("the principle is", p)
    print("the time period is", t)
    print("the rate of interest is", r)

    si = (p * t * r)/100
    # print("the simple interest is", si)
    return si

# Driver code
var = simple_interest(8,6,8)
print(var)



