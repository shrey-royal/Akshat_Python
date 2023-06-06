'''
Args and Kwargs
> *args: arguments: tuple: positional arguments (non-keyword arguments)
> **kwargs: keyword arguments: dictionary: keyword arguments (keyword arguments)

the use of *args and **kwargs is to allow a function to take a variable number of arguments

'''

# def sum(*numbers):
#     result = 0
#     for number in numbers:
#         result += number    
#     return result

# print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(sum(1, 2, 3, 3))

# def print_kwargs(**pappu):
#     print(pappu)

# print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)

def employee(**data):
    print(data)
    print(type(data))
    print(data["name"])
    print(data["age"])
    print(data["salary"])
    print(data["designation"])
    print(data["experience"])
    print(data["address"])
    print(data["phone"])
    print(data["email"])

employee(name="John", age=30, salary=25000, designation="Manager", experience=5, address="Bangalore", phone=9876543210, email="abc@gmail.com")

'''
1. Create a function that takes n number of arguments and return the following things:
    a. Sum of all the arguments
    b. Maximum of all the arguments
    c. Minimum of all the arguments
    d. Average of all the arguments
    e. Concatenation of all the arguments

sample input: 1, 2, 3, 4, 5
sample output: 
    Sum: 15
    Maximum: 5
    Minimum: 1
    Average: 3
    Concatenation: 12345

'''