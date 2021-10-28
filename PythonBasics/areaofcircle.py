# Area of a circle can simply be evaluated using following formula.
#
# Area = pi * r2
# where r is radius of circle


def findArea(r):
    PI = 3.14
    return PI * (r * r)

# Driver code
print("area is %.6f" % findArea(5))
