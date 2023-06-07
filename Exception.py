'''
Exception is an error that happens during execution of a program. When that error occurs, Python generate an exception that can be handled, which avoids your program to crash.

try block is the block of code to be attempted (may lead to an error). the try block is executed, the except block is skipped. If there is an error in the try block, the except block will execute.

finally block is a block of code that will always execute regardless of there is an exception in the try block or not.

else block is executed if there is no exception raised.

syntax:
try:    # mandatory
    # code block
except:   # optional
    # code block
else:    # optional
    # code block
finally:    # optional # always executed
    # code block

Exception Handling in Python:
    1. try
    2. except
    3. else
    4. finally
    5. raise
'''
# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except Exception as err:
#     print(err)
# # except:
#     # print("Invalid Input")

# print("Abcd")
# -----------------------------------------------------
# try:
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     if b == 0:
#         raise ZeroDivisionError("b can't be zero")
#     c = a / b
#     print(c)

# except ZeroDivisionError as e:
#     print("Can't divide by zero")
#     print("ZeroDivisionError -> ", e)

# except ValueError as e:
#     print("Invalid Input")
#     print("ValueError -> ", e)

# except Exception as e:
#     print("Something went wrong...")
#     print("Exception -> ", e)

# except (ZeroDivisionError, ValueError) as e:
#     print("Error -> ", e)

# -----------------------------------------------------

name = input("Enter your name: ")

try:
    if name == "Jay" or name == "jay":
        raise ValueError(f"{name} sir is working at Royal, so he is not allowed to join other companies.")
    else:
        print("Welcome ", name)

except ValueError as e:
    print(e)

finally:
    print("Thank you for visiting our company.")

