# Variables in Python

name = "Dheeraj"
age=29
money=100.50
is_married= False
x = None

company="Infosys"
# print(Company) # Error ---> Python is case-sensitive



# Type Checking
print(type(name))        #Output : <class 'str'>      --> String
print(type(age))         #Output : <class 'int'>      --> int
print(type(money))       #Output : <class 'float'>    --> float
print(type(is_married))  #Output : <class 'bool'>     --> boolean
print(type(x))           #Output : <class 'NoneType'> --> None     --> Very useful in AI / APIs later




# Input and Output
name = input("Enter Your Name: ") # Input is ALWAYS string and always returns a string
print(name)
print("Hi", name)

age = input("Enter the age: ") 
print(age) 
print(type(age)) # <class 'str'>





# Conversion from one data type to other ---> just mention the data type u want to convert to
weight=int(input("Enter the weight: "))
# NOTE:What if u put string in this ---> crash ---> valueError: invalid literal for int() with base 10 
print(weight) 
print(type(weight)) # <class 'int'>

# Safer Version 1: To avoid crash if user enters a string where numer is expected
salary = input("Enter the salary: ")
if salary.isdigit(): 
    salary = int(salary)
    print("Salary is: ", salary)
else:
    print("Invalid Input")

# Safer Version 2 (better): .isdigit() is good, but limited as it doesn't handle negative numbers and decimals
salary = input("Please enter your salary: ")
try :
    salary = int(salary)
    if(salary<0):
        print("Salary can not be negative")
    else:
        print("The salary is: ", salary)
except ValueError:
    print("Invalid Input")
# NOTE" This works, but not best practice ---> as we learn more we will see how to handle




# String Mutability
player="Virat"
print("Character at 0 index: ",player[0]) # Output : V
# player[0]= 'K' # Error ---> str' object does not support item assignment
print("Character at 0 index: ",player[0]) # Output : V

#Correct way 
player= "K"+ player[1:]
print("Character at 0 index: ",player[0]) # Output : K






# Multiple Assignment 
a,b,c,d=10,20,30,40
# a,b,c,d=10,20,30,40,50,60,70  # Error ---> ValueError: too many values to unpack (expected 4, got 7)
print("a: ",a)
print("b: ",b)
print("c: ",c)
print("d: ",d)

# NOTE: we can use * for extra values
p, q, *rest = 100, 200, 300, 400, 500, 600
print("p: ",p) # 100
print("q: ",q) # 200
print("rest: ",rest) # Ouput: rest: [300, 400, 500, 600]






# NOTE: # NOTE: In JavaScript we use backticks (`) for template literals but in Python we use f-strings
car="Maruti"
print(f"car is {car}") # Output: car is Maruti





# Introduction Summary : 
# 1. No need to declare data types --> Python is dynamically typed
# 2. Variables can be reassigned with new values and types ---> Reassignment is possible
# 3. input() always returns string. Hence for numeric input Type conversion is needed.
# 4. Python is case-sensitive
# 5. Use try-except for safe input handling
# 6. Multiple assignment is supported (* for extra values)
# 7. f-strings are used for formatted output
# 8. None is Python’s null type
