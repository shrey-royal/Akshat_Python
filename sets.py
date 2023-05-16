"""
List[] -> Indexed, Ordered, Changeable, Allows Duplicates
Tuple() -> Indexed, Ordered, Unchangeable, Allows Duplicates
Set{} -> Unindexed, Unordered, Changeable, No Duplicates
Dictionary{} -> Indexed, Unordered, Changeable, No Duplicates in key, Allows Duplicates in value

set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

example: set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

"""


# numbers = {234, 123, 345, 34, 78, 45, 999, 132, 556, 435, 678}
# names = {"John", "Bob", "Alice", "John", "Bob", "Alice"}

# print(numbers)
# print(names)

# print(type(numbers))
# print(type(names))

# print(len(numbers))
# print(len(names))

# print(994 in numbers)

# print(type(numbers) is type(names))
# print(type(numbers) is set)

# set methods
# print(numbers, end="\n\n")
# add()
# numbers.add(994)
# print(numbers)

"""
How to take random numbers in python

import random
rand_nums = random.sample(range(1, 100), 20)    

example:

import random
rand_nums = random.sample(range(1, 100), 20)

print(rand_nums, end="\n\n")


"""

# discard()
# numbers.discard(345)
# print(numbers)

# difference() -> returns a set containing the difference between two or more sets

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

print(set1, set2, sep="\n")


# set3 = set1.difference(set2)
# print(set3)
# set4 = set2.difference(set1)
# print(set4)

# difference_update() -> removes the items in this set that are also included in another, specified set

# set1.difference_update(set2)
# print(set1)

# intersection() -> returns a set, that is the intersection of two other sets
# set3 = set1.intersection(set2)
# print(set3)

# intersection_update() -> removes the items in this set that are not present in other, specified set(s)

# set1.intersection_update(set2)
# print(set1)

# isdisjoint() -> Return True if two sets have a no intersection otherwise False
# print({234, 223}.isdisjoint(set2))    # True
# print(set1.isdisjoint(set2))    # False

# issubset() -> Returns whether another set contains this set or not
# print(set1.issubset(set2))    # False
# print({1, 2, 3, 4, 5}.issubset(set1))    # True

# issuperset() -> Returns whether this set contains another set or not
# print(set1.issuperset(set2))    # False
# print({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}.issuperset(set2))    # True

# symmetric_difference() -> returns a set with the symmetric differences of two sets

# set3 = set1.symmetric_difference(set2)
# print(set3)

# symmetric_difference_update() -> inserts the symmetric differences from this set and another

# set1.symmetric_difference_update(set2)
# print(set1)

# union() -> Return a set containing the union of sets

# set3 = set1.union(set2)
# print(set3)

# update() -> Update the set with the union of this set and others

# set1.update({'a', 'b'})
# print(set1)

# pop() -> removes an element from the set

# set1.pop()
# print(set1)

# remove() -> removes the specified element

# set1.remove(8)
# print(set1)

# clear() -> removes all the elements from the set

# set1.clear()
# print(set1)

# del -> deletes the set completely

# del set1
# print(set1)

# copy() -> returns a copy of the set

# set3 = set1.copy()
# print(set3)



"""
Task:- 

1. Find the size of a Set in Python  
> find the size of set

2. Iterate over a set in Python
> iterate over a set using for loop

3. Python - Maximum and Minimum in a Set
> find the maximum and minimum value in a set

4. Python - Remove items from Set
> remove items from a set

5. Python - Check if two lists have at-least one element common
> check if two lists have at-least one element common

6. Python program to find common elements in three lists using sets
> find common elements in three lists using sets

7. Python - Find missing and additional values in two lists
> find missing and additional values in two lists

8. Python program to find the difference between two lists
> find the difference between two lists

9. Python Set difference to find lost element from a duplicated array
> find lost element from a duplicated array

10. Python program to count number of vowels using sets in given string
> count number of vowels using sets in given string

11. Concatenated string with uncommon characters in Python
> Concatenated string with uncommon characters in Python

12. Python - Program to accept the strings which contains all vowels
> Program to accept the strings which contains all vowels

"""