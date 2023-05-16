# Single Line comment
'''
Multi 
line 
comments
'''

"""
multi 
line 
comments
"""

'''
Basics of Python:

Q. What is Python?
Ans. Python is a high level, interpreted, interactive and object-oriented scripting language.
-> high level: Python is designed to be easy to read and simple to implement.
-> interpreted: Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. This is similar to PERL and PHP.
-> interactive: You can actually sit at a Python prompt and interact with the interpreter directly to write your programs.

Q. What are the features of Python?
Ans. Following are the important features of Python - 
-> Easy-to-learn: Python has few keywords, simple structure, and a clearly defined syntax. This allows the student to pick up the language quickly.
-> Easy-to-read: Python code is more clearly defined and visible to the eyes.
-> Easy-to-maintain: Python's source code is fairly easy-to-maintain.
-> A broad standard library: Python's bulk of the library is very portable and cross-platform compatible on UNIX, Windows, and Macintosh.
-> Interactive Mode: Python has support for an interactive mode which allows interactive testing and debugging of snippets of code.
-> Portable: Python can run on a wide variety of hardware platforms and has the same interface on all platforms.
-> Extendable: You can add low-level modules to the Python interpreter. These modules enable programmers to add to or customize their tools to be more efficient.
-> Databases: Python provides interfaces to all major commercial databases.
-> GUI Programming: Python supports GUI applications that can be created and ported to many system calls, libraries and windows systems, such as Windows MFC, Macintosh, and the X Window system of Unix.
-> Scalable: Python provides a better structure and support for large programs than shell scripting.
-> Embeddable: You can embed Python into an application to give your application a programmable interface.

'''

# Basic Print Statement

# print("Hello World")
# print("Akshat", "Chaturvedi", "Studies at PDEU")
# print("abcd", 1234, 12.34, True, False, None)
# print("abcd", 1234, 12.34, True, False, None, sep="|")
# sep(separator) is used to separate the values with the given separator
# print("akshat", sep="|")  # doesn't work as there is only one value

# print("Akshat \n\tChaturvedi")
# print("Student at", end=" ") # at the end of the print statement, a new line is added
# # end has default value as \n(new line)
# print("PDEU")

# print("Akshat", end="\t")
# print("Chaturvedi")

# variables and data types

# data types
# int, float, bool, str, None, list, tuple, set, dict, complex

# a = 10
# b = 20.2
# c = True
# d = "Akshat ejibwehoifw  hfioi weofh iowe oew  io oiwh woi weuh ouiweh io"
# e = None
# f = 2 + 3j  # complex number
# more complex example
# g = 2 + 3j
# h = 3 + 4j
# i = g + h
# print(i)

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))
# print(e, type(e))
# print(f, type(f))

# a = None
# print(a, type(a), id(a))

# a = 6
# print(a, type(a), id(a))

# a = 6.2
# print(a, type(a), id(a))

# how to get the memory bytes of a variable
# id() function is used to get the memory address of a variable
# print(a, type(a), id(a))

# how to know the memory of a variable
# sys.getsizeof() function is used to get the memory bytes of a variable
# import sys  # sys is a module

# _int = 10
# print("Size of int is ", sys.getsizeof(_int)) # 24 bytes

# _float = 10.2
# print("Size of float is ", sys.getsizeof(_float)) # 24 bytes

# _bool = True
# print("Size of bool is ", sys.getsizeof(_bool)) # 28 bytes

# _str = "Akshat"
# print("Size of str is ", sys.getsizeof(_str)) # 55 bytes

# _none = None
# print("Size of None is ", sys.getsizeof(_none)) # 16 bytes

# _complex = 2 + 3j
# print("Size of complex is ", sys.getsizeof(_complex)) # 32 bytes

# user input -> input() function
# input() function always take input as string
# type casting is required to convert the input into the desired data type

# a = int(input("Enter a number: "))
# print(a, type(a))

# name = input("Enter your name: ")
# print("Hello", name)

# a = float(input("Enter a number: "))
# print(a, type(a))

'''
Tasks:
1. Take input from the user and print the following:
    a. Name
    b. Age
    c. Height
    d. Weight

2. Take input from the user and print the following:
    a. Name
    b. Salary
    c. Age
    d. Department
    e. Designation
    f. Experience

3. Take input from the user of 2 numbers and print the following:
    a. Sum
    b. Difference
    c. Product
    d. Quotient
    e. Remainder

'''