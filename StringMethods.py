string = "Royal Technosoft Pvt. Ltd."

# methods from a to z

# print("Length of the string is: ", len(string)) # it will print the length of the string
# print(string.capitalize()) # it will capitalize the first letter of the string
# print(string.casefold()) # it will convert the string into lower case
# print(string.center(50, "-")) # it will center the string
# print(string.count(".")) # it will count the number of times the string is present in the string
# print("Royal tech fʁɑ̃sɛ".encode(encoding="ASCII", errors="namereplace")) # it will encode the string
'''
encode() method returns encoded version of the string.

Syntax: string.encode(encoding='UTF-8', errors='strict')

Parameters:
encoding: It is a string representing the encoding to be used. Default encoding is 'UTF-8'.
errors: It is a string specifying how to handle encoding errors. Default is 'strict'.

errors: 
strict: It will raise a ValueError exception if there is an encoding error.
ignore: It will ignore the encoding error.
replace: It will replace the encoding error with a question mark.
xmlcharrefreplace: It will replace the encoding error with XML character reference.
backslashreplace: It will replace the encoding error with backslash and unnamed unicode character.
namereplace: It will replace the encoding error with backslash and named unicode character.
'''

# print(string.endswith("Ltd.")) # it will check if the string ends with the given string
# print("Hello\tWorld\t.".expandtabs(4)) # it will expand the tabs in the string
# print(string.find("Technosoft")) # it will find the index of the given string
# print("My name is {}".format("Khan")) # it will format the string
# print(string.index("Technosoft")) # it will find the index of the given string
# print("123string".isalnum()) # it will check if the string is alphanumeric
# print("string123".isalpha()) # it will check if the string is alphabetic
# print("123".isdecimal()) # it will check if the string is decimal
# print("123".isdigit()) # it will check if the string is digit
# print("123".isnumeric()) # it will check if the string is numeric
# print(" ".isspace()) # it will check if the string is space
# print("string".istitle()) # it will check if the string is title if the first letter is capital then it will return true otherwise false
# print("STRING".isupper()) # it will check if the string is upper case
# print("string".islower()) # it will check if the string is lower case
# print("string".join("123")) # it will join the string with the given string
# print("string".ljust(50, "-")) # it will left justify the string
# print("String".lower()) # it will convert the string into lower case
# print("                                     String".lstrip()) # it will remove the spaces from the left side of the string
# print("String".partition("i")) # it will partition the string
# print("String".replace("i", "o")) # it will replace the string with the given string
# print("string".rfind("i")) # it will find the index of the given string from the right side
# print("string".rindex("i")) # it will find the index of the given string from the right side
# print("string".rjust(50, "-")) # it will right justify the string
# print("string".rpartition("i")) # it will partition the string from the right side
# print("string".rsplit("i")) # it will split the string from the right side
# print("string                                         ".rstrip()) # it will remove the spaces from the right side of the string
# print("string".split("i")) # it will split the string
# print("string\nuaihfisdbf\nayvduaedf\nend".splitlines()) # it will split the lines of the string
# print("string".startswith("r")) # it will check if the string starts with the given string
# print("                  string                  ".strip()) # it will remove the spaces from both the sides of the string
# print("sTrIng".swapcase()) # it will swap the case of the string
# print("string".title()) # it will convert the string into title case
# print("string".upper()) # it will convert the string into upper case
# print("string".zfill(50)) # it will fill the string with zeros

'''
Tasks:

1. Write a program to check if the given string is palindrome or not.
'''