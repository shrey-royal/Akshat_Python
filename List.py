'''
List is a collection which is ordered and changeable. Allows duplicate members.
list in python is a class, so we can create a list object by using the list() function.

syntax: 
list_name = [item1, item2, item3, item4, item5]

types of declaration:
1. list_name = [item1, item2, item3, item4, item5]
2. list_name = list((item1, item2, item3, item4, item5))
3. list_name = list([item1, item2, item3, item4, item5])
4. list_name = list({item1, item2, item3, item4, item5})


we can store any type of data in a list
ex:
list_name = [1, 2, 3, 4, 5, "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", True, False, 1.1, 2.2, 3.3, 4.4, 5.5]

'''

# list declaration
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits)
# print(type(fruits))
# print(f"Length of the list: {len(fruits)}")

# accessing list items
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# accessing list items using negative indexing
# print(fruits[-1])
# print(fruits[-2])
# print(fruits[-3])

# accessing list items using range of indexes
# print(fruits[2:5])
# print(fruits[:4])
# print(fruits[2:])
# print(fruits[-4:-1])

# accessing list items using range of indexes with step
# print(fruits[1:6:2])
# print(fruits[::2])
# print(fruits[1::2])
# print(fruits[::-1])

# changing list items
# fruits[1] = "berry"
# print(fruits)

# looping through a list
# for i in fruits:
#     print(i)

# checking if an item exists
# f = input("Enter the fruit name you want to search: ")
# if f in fruits:
#     print(f"Yes, {f} is in the fruits list")
# else:
#     print(f"No, {f} is not in the fruits list")

# adding items to a list
# fruits.append(input("Enter the fruit name you want to add: "))
# print(fruits)

# adding items to a list using insert() method
# fruits.insert(int(input("Enter the index you wnat to add the fruit of ")), input("Enter the fruit name you want to add: "))
# print(fruits)

# adding items to a list using extend() method
# fruits.extend(["grapes", "papaya", "pineapple"])
# print(fruits)

#  List Methods in Python

# 1. append() method - adds an item to the end of the list
# fruits.append("grapes")
# print(fruits)

# 2. clear() method - removes all the items from the list
# fruits.clear()
# print(fruits)

# 3. copy() method - returns a copy of the list
# fruits_copy = fruits.copy()
# print(fruits_copy)

# 4. count() method - returns the number of elements with the specified value
# fruits.append("apple")
# print(fruits.count("apple"))
# print(fruits)

# 5. extend() method - add the elements of a list (or any iterable), to the end of the current list
# new_fruits = ["grapes", "papaya", "pineapple"]
# fruits.extend(new_fruits)
# print(fruits)

# 6. index() method - returns the index of the first element with the specified value
# print(fruits.index("mango"))   # return value error if the value is not present in the list

# 7. insert() method - adds an element at the specified position
# fruits.insert(2, "berry")
# print(fruits)

# 8. pop() method - removes the element at the specified position
# print(fruits.pop(2))
# print(fruits)

# 9. remove() method - removes the item with the specified value
# fruits.remove("melon")
# print(fruits)

# 10. reverse() method - reverses the order of the list
# fruits.reverse()
# print(fruits)

# 11. sort() method - sorts the list
# fruits.sort()
# print(fruits)

# 12. len() method - returns the length of the list
# print(len(fruits))

# 13. max() method - returns the largest item in the list
# print(max(fruits))

# 14. min() method - returns the smallest item in the list
# print(min(fruits))

# 15. sum() method - returns the sum of all items in the list
# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))

# 16. any() method - returns True if any item in an iterable are true, otherwise it returns False
# print(any([]))

