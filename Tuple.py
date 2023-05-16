'''
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

syntax: tuple = (1,2,3,4,5,6,7,8,9,10)

Advantages of Tuple over List:
1. Tuple is faster than list.
2. Tuple consumes less memory than list.
3. Tuple is immutable, so it is safer than list.
'''

numbers = (1,2,3,4,5,6,7,8,9,10)

# print(numbers)
# print(type(numbers))
# print(id(numbers))

# Accessing Tuple

# print(numbers[7])
# print(numbers[1:5])
# print(numbers[-1])
# print(numbers[::-1])
# print(numbers[::2])
# print(numbers[1::2])

# Changing Tuple Values
# numbers[0] = 100

# Deleting Tuple
# del numbers
# print(numbers)


# we can't add or remove items from tuple
# we can't swap values in tuple


myList = list(numbers)
# for i in numbers:
#     print(i)
#     myList.append(i) 

print(myList)

print(tuple(myList))

# we can convert tuple to list and list to tuple but while converting the list to tuple we can't use append method.

# Tuple Methods

myTup = (1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10)

# count(element) - returns the number of times the element is present in the tuple
# print(myTup.count(5))

# index(element) - returns the index of the element
# print(myTup.index(10))

# len(tuple) - returns the length of the tuple
# print(len(myTup))

