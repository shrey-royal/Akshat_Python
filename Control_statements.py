'''
Control statements are used to control the flow of execution of a program.
Python supports the following control statements:
1. if
2. if-else
3. if-elif-else
4. for
5. while
6. break
7. pass
8. continue
'''

# if statement
# if statement is used to check if a condition is true or false.
# If the condition is true, the statements inside the if block are executed.
# If the condition is false, the statements inside the if block are skipped.
# Syntax:
# if condition:
#     statements

# Example:
# a = 10
# if a > 5:
#     print("a is greater than 5")

# Output:
# a is greater than 5

# if-else statement
# if-else statement is used to check if a condition is true or false.
# If the condition is true, the statements inside the if block are executed.
# If the condition is false, the statements inside the else block are executed.
# Syntax:
# if condition:
#     statements
# else:
#     statements

# Example:
# a = 10
# if a > 15:
#     print("a is greater than 15")
# else:
#     print("a is less than 15")

# Output:
# a is less than 15

# if-elif-else statement
# if-elif-else statement is used to check if a condition is true or false.
# If the condition is true, the statements inside the if block are executed.
# If the condition is false, the statements inside the elif block are executed.
# If the condition is false, the statements inside the else block are executed.
# Syntax:
# if condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

# Example:
# a = 10
# if a > 15:
#     print("a is greater than 15")
# elif a > 12:
#     print("a is greater than 12")
# else:
#     print("a is less than 12")

# Output:
# a is less than 12

# for statement
# for statement is used to iterate over a sequence.
# Syntax:
# for variable in sequence:
#     statements

# Example:
# for i in range(1, 11, 2):  # range(1, 11) returns a sequence of numbers from 1 to 10
#     print(i, end=", ")

# while statement
# while statement is used to iterate over a sequence.
# Syntax:
# while condition:
#     statements

# Example:
# i = 1
# while i <= 10:
#     print(i, end=", ")
#     i += 1

# break statement
# break statement is used to terminate the loop.
# Syntax:
# for variable in sequence:
#     statements
#     break

# Example:
# for i in range(1, 11):
#     print(i, end=", ")
#     if i == 5:
#         break


# pass statement
# pass statement is used to skip the statements.
# Syntax:
# for variable in sequence:
#     pass

# Example:
# for i in range(1, 11):
#     pass    # pass statement skips the statements

# continue statement
# continue statement is used to skip the statements.
# Syntax:
# for variable in sequence:
#     statements
#     continue

# Example:
# for i in range(1, 11):
#     if i == 5:
#         continue    # continue statement skips the current iteration and continues the next iteration
#     print(i, end=", ")


# pass statement basically tells the interpreter to do nothing. It is used as a placeholder. It is used when a statement is required syntactically but you do not want any command or code to execute.

# continue statement is used to skip the current iteration and continues the next iteration.



# Grade sheet

# math = int(input("Enter the marks of math: "))
# eng = int(input("Enter the marks of english: "))
# sci = int(input("Enter the marks of science: "))
# sst = int(input("Enter the marks of sst: "))
# hindi = int(input("Enter the marks of hindi: "))
# total = math + eng + sci + sst + hindi
# avg = total / 5
# print("Total marks: ", total)
# print("Average marks: ", avg)
# if avg >= 90 and avg <= 100:
#     print("Grade: A")
# elif avg >= 80 and avg < 90:
#     print("Grade: B")
# elif avg >= 70 and avg < 80:
#     print("Grade: C")
# elif avg >= 60 and avg < 70:
#     print("Grade: D")   
# else:
#     print("Grade: F")


# hotel management system with price calculation

# print("Welcome to Our Hotel")
# print("1. Check in")
# print("2. Check out")
# print("3. Exit")
# choice = int(input("Enter your choice: "))

# if choice == 1:
#     print("Welcome to our hotel")
#     print("1. Single room")
#     print("2. Double room")
#     print("3. Triple room")
#     print("4. Quad room")
#     room = int(input("Enter your choice: "))
#     if room == 1:
#         print("Single room")
#         print("1. AC")
#         print("2. Non-AC")
#         ac = int(input("Enter your choice: "))
#         if ac == 1:
#             print("AC room")
#             days = int(input("Enter the number of days: "))
#             print("Total price: ", days * 2000)
#         elif ac == 2:
#             print("Non-AC room")
#             days = int(input("Enter the number of days: "))
#             print("Total price: ", days * 1000)

#     elif room == 2:
#         print("Double room")
#         print("1. AC")
#         print("2. Non-AC")
#         ac = int(input("Enter your choice: "))
#         if ac == 1:
#             print("AC room")
#             days = int(input("Enter the number of days: "))
#             print("Total price: ", days * 4000)
#         elif ac == 2:
#             print("Non-AC room")
#             days = int(input("Enter the number of days: "))
#             print("Total price: ", days * 2000)

#     elif room == 3:
#         print("Triple room")
#         print("1. AC")
#         print("2. Non-AC")
#         ac = int(input("Enter your choice: "))
#         if ac == 1:
#             print("AC room")
#             days = int(input("Enter the number of days: "))
#             print("Total price: ", days * 6000)
#         elif ac == 2:
#             print("Non-AC room")
#             days = int(input("Enter the number of days: "))
#             print("Total price: ", days * 3000)

#     elif room == 4:
#         print("Quad room")
#         print("1. AC")
#         print("2. Non-AC")
#         ac = int(input("Enter your choice: "))
#         if ac == 1:
#             print("AC room")
#             days = int(input("Enter the number of days: "))
#             print("Total price: ", days * 8000)
#         elif ac == 2:
#             print("Non-AC room")
#             days = int(input("Enter the number of days: "))
#             print("Total price: ", days * 4000)

# elif choice == 2:
#     print("Thank you for visiting our hotel")

# elif choice == 3:
#     print("Thank you for using our services")


# Car rental system with price calculation and discount calculation

# Loops problems


# for i in range(1, 6):   # outer loop is used to print the rows
#     for j in range(1, i+1): # inner loop is used to print the columns
#         print(f"{j}", end=" ")
#     print() # print() is used to print a new line

# (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), 
# (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), 
# (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), 
# (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), 
# (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), 
    


# 1. Write a program to print the following pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

# 2. Write a program to print the following pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
