'''
Dictionary is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key`s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.


Dictionary is unordered, so you can not be sure in which order the items will appear.

# key-value pairs -> key:value

# creating a dictionary
dictionary_name = {key1:value1, key2:value2, key3:value3, ...}

# accessing values in a dictionary
dictionary_name[key] -> to get the value of the key
dictionary_name.get(key) -> to get the value of the key

# adding new key-value pairs
dictionary_name[newKey] = newValue  -> to add a new key-value pair
# if the key already exists, the value will be updated to the new value otherwise a new key-value pair will be added

# removing key-value pairs
# del dictionary_name[key] -> to remove a key-value pair
dictionary_name.pop(key) -> to remove a key-value pair

'''

# creating a dictionary
myDict = {
    "fruits" : ["apple", "banana", "orange"],
    "vegetables" : ["potato", "tomato", "cucumber"],
    "numbers" : [1, 2, 3, 4, 5],
    2 : "this is two",
    1.2 : "this is one point two"
}

# print(myDict)

# dictionary methods

# myDict.clear() # -> to remove all the key-value pairs
# print(myDict)

# print(myDict.copy()) # -> to copy the dictionary

# newDict = {}
# print(newDict.fromkeys("12", "shrey")) # -> to create a new dictionary with the given keys and values

# print(myDict.get("vegetables")) # -> to get the value of the key

# print(myDict.items()) # -> to get the key-value pairs as a list of tuples

# print(myDict.keys()) # -> to get the keys of the dictionary

# print(myDict)
# print(myDict.pop("numbers")) # -> to remove the key-value pair with the given key
# print(myDict)

# print(myDict)
# print(myDict.popitem()) # -> to remove the last key-value pair
# print(myDict)

# print(myDict.setdefault(1.2, "abcd")) # -> to get the value of the key
# setdefault will add the key-value pair if the key does not exist in the dictionary, or if the key exists, it will return the value of the key
# print(myDict)

# print(myDict.update({1.2: 1}))  # -> to update the value of the key
# print(myDict)

# print(myDict.values()) # -> to get the values of the dictionary

# for i in myDict:
#     print(i, myDict[i], sep=": ")

# for key, value in myDict.items():
#     print(key, value, sep=" : ")

# for key in myDict.keys():
#     print(key)

# for value in myDict.values():
#     print(value)


"""
Dictionary tasks:

1. Check if a Given Key Already Exists in Dictionary
-> If you have learned about Python dictionaries, you will know that you can check if a given key exists or not in multiple ways. 

D1 = {'first_name' : 'Krutarth', 'age' : 22, 'height' : 5.0 , 'job' : 'Developer', 'company': 'Google'}

2. Handle Missing Keys in Dictionary
-> Dictionary is a collection in python, where the data is stored in the form of a key-value pair, that is, it maps key to its value. Often, you will not know all the keys present in the dictionary and you might end up with a typing error which may lead to runtime error due to missing keys in the dictionary.

D1 = {'first_name' : 'Zafar', 'age' : 21, 'height' : 4.8 , 'job' : 'Engineer', 'company': 'Microsoft'}

3. Extract Unique Values in a Given Dictionary
-> In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

D1 = {	'list1': [4, 7, 10, 20], 
      	'list2': [7, 16, 9, 10], 
     	'list3': [13, 10, 4, 8], 
     	'list4': [7, 20, 6, 11]
         }

Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]

4. Print the Sum of Key Value Pairs in a Given Dictionary
-> You need to create a list which has the sum of key-value pairs of a given dictionary. 

D1 = {2: 8, 5: 20, 3: 15}

HINT-> This can be done using a for loop and append() function. 

5. Replace Dictionary Values From Other Dictionary
-> Let’s say you are given two dictionaries. You need to write a python program that will replace the values in the first dictionary with the values from the second dictionary if the key is present in the second dictionary. 

# initializing D1 - first dictionary
D1 = {'first_name' : 'Rutvi', 'age' : 21, 'height' : 4.0 , 'job' : 'Software Engineer', 'company': 'Uber'}
 
# initializing D2 - - first dictionary
D2 = {'age' : 35, 'job' : 'senior data analyst'}

6. Update or Change the Keys in a Given Dictionary
-> try these 2 ways
i)  Using assignment operator
ii) Using pop() method

D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

7. Delete a List of Keys in a Given Dictionary 

8. Count the Frequency of List Items Using a Dictionary
-> You can solve this in many ways. Any ideas? Well, you can just use looping constructs or use the list() count method or you can start with an empty dictionary and use the dict.get() method. Probably many other ways!

D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

9. Change the Value of a Key in Nested Dictionary
-> Given a nested dictionary, you need to write a program demonstrating how to change the value associated with a particular key of that dictionary. 

#change the value of a key in nested dictionary
#Initializing Dictionary
D1 = {'emp1': {'name' : 'Niraj', 'age' : 21, 'job' : 'developer'}, 
      'emp2': {'name' : 'Zafar', 'age' : 22, 'job' : 'data analyst'}, 
      'emp3': {'name' : 'Rutvi', 'age' : 22, 'job' : 'data scientist'}, 
      'emp4': {'name' : 'Krutarth', 'age' : 60, 'job' : 'python developer'}}

11. Check if the Given Dictionary Is Empty or Not
-> One way to check this using the len() function, which you can try coding; we will achieve this using the bool() function. The bool() function evaluates to standard true or false and is used to return or convert a value to Boolean type. If you pass an empty dictionary, the bool() evaluates to False, as failure to convert something that is empty.

14. Get a Key From Value in a Dictionary
-> You need to write a program, which returns the key for a given value. This can be done in multiple ways. Try doing it using dict.items() function.

#get key for a given value using dict.items()
# Dictionary Initialization
D1 = {'Priyanka Chopra': 23, 'Alia Bhatt': 29, 'Hritik Roshan': 45, 'Ranbir Kapoor': 40}

15. Sort a Given Dictionary by Key
-> You know this so, you got this...

D1 = {'Niraj': 23, 'Jaynam': 29, 'Rutvi': 40, 'Zafar': 45, 'Obama': 34}


"""