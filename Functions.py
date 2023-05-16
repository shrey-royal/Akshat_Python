"""
Functions in python are defined using the def keyword.

Functions are objects in python, and can be assigned to variables, passed as arguments to other functions, and returned from other functions.

there are 4 types of user-defined functions in python:
1. Function with no arguments and no return value
2. Function with arguments and no return value
3. Function with no arguments and return value
4. Function with arguments and return value

def function1():
    print("Hello World")

function1()


"""



# Function with no arguments and no return value

def add():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Sum is: ", a+b)

def sub(a, b):
    print("Difference is: ", a-b)

def mul():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return a*b

def div(a, b):
    return a/b


a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")
choice = int(input("Enter your choice: "))

if choice == 1:
    add()

elif choice == 2:
    sub(a, b)

elif choice == 3:
    print("Multiplcation is: ", mul())

elif choice == 4:
    print("Division is: ", div(a, b))

else:
    print("Invalid Choice")


"""
tasks to be done:

1. Write a function to find the factorial of a number.
2. Write a function to find the sum of digits of a number.
3. Write a function to find the reverse of a number.
4. Write a function to find the sum of all the numbers in a list.
5. Write a function to find the largest number in a list.
6. Write a function to find the smallest number in a list.

"""