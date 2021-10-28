#Python Program for compound interest
# Formula to calculate compound interest annually is given by:
# A = P(1 + R/100) t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span

# Example :
# Input : Principle (amount): 1200
#         Time: 2
#         Rate: 5.4
# Output : Compound Interest = 133.099243


def compount_interest(p,r,t):

    print("the principle amount is", p)
    print("the rate of interest is", r)
    print("the time span is ", t)
#Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
    a = p * (pow(  (1 + r/100), t ))
    CI = a - p

    print("the compound interest is ", CI)
    return CI
#Driver Code

New_ci = compount_interest(10000, 10.25, 5)
print(New_ci)



