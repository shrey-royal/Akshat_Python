# name = input("Enter your name: ")   # type cast
# print("Hello, " + name + "!")   # concatenation
# print(f"Hello, {name}!")   # f-string
# print("Hello, {}!".format(name))   # format method
# print("Hello, %s!" % name)   # old style

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello, " + name + "! You are " + str(age) + " years old.")
# print(f"Hello, {name}! You are {age} years old.")
# print("Hello, {}! You are {} years old.".format(name, age))
# print("Hello, %s! You are %d years old." % (name, age))

# print(f"Addition of {2} and {3} is {2 + 3}.")

string = "Hello,_My_name_is_John."
# print(string[10])
# print(len(string))  # length of string

# slicing of string -> [start:stop:step]
'''
start -> starting index -> default = 0
stop -> ending index    -> default = len(string) - 1
step -> increment   -> default = 1

# positive indexing
Hello, My name is John.
0123456789.............

# start -> 0
# stop -> len(string)
# step -> 1

# negative indexing
Hello, My name is John.
.............987654-3-2-1

# start -> -1
# stop -> -len(string) - 1
# step -> -1

'''
# print(string)
# print(string[0:7])  # Hello
# print(string[-5:])  # John.
# print(string[0:7:2])  # Hlo

# store the name John in a variable
# name = string[-5:-1]
# print("Your name is", name)

# print(string[::-1]) # reverse the string


'''
Tasks on Strings and Slicing

1. Store your name in a variable and print it in reverse order.
2. Store your name in a variable and print it in reverse order with every second letter.
3. Scan name and age from the user and print it in the following format:
    Hello, <name>! You are <age> years old.
4. Scan name and age from the user and print it in the following format:
    Hello, <name>! You are <age> years old. You will turn 100 years old in <year>.

5. Scan name, age, salary in one string and then slice the name and print it in the following format:
    Hello, <name>! You are <age> years old. Your salary is <salary>.

----
negative indexing tasks
6. take input of number(2 digits) from the user and print the sum of the digits.
7. take input of string and print the last half of the string.
8. print every n character of the string. and n and string will be scanned from the user.
9. take input of string and print first n and last n characters of the string using negative indexing. n will be scanned from the user. 
'''

