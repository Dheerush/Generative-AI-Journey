#  ====================================== Functions in Python ==========================================
def greet(name):
    print(f"Hello {name}, have a nice day.")

greet("Dheeraj")


# function to check whether a number is even or odd
def checkNumber(num):
    if num%2==0:
        print(f"{num} is EVEN")
    else:
        print(f"{num} is ODD")


checkNumber(24)
checkNumber(21)


# Default Arguments 
# Rule: All default parameters must come AFTER non-default parameters
def calculateAmount(p,t,r=10):
    return (p*r*t)/100

print(calculateAmount(1000, 2))       # r = default (10)
print(calculateAmount(1000, 2, 5))    # r = 5