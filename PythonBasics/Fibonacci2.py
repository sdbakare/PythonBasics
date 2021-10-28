# Function for nth fibonacci number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1

Fibarray = [0,1]

def fibonacci(n):
    print("Initial n number is", n)
    if n < 0:
        print("Incorrect Input")
    elif n<= len(Fibarray):

        return Fibarray[n-1]
    else:
        tempfib = fibonacci(n-1) + fibonacci(n-2)
        Fibarray.append(tempfib)
        print(Fibarray)
        return tempfib

# Driver Program
print(fibonacci(9))
print(Fibarray)
