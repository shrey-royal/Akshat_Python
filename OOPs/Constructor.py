'''
Constructors in python are the methods which are used to initialize the instance variables of the class.

There are two types of constructors in python.
1. Default Constructor (non parameterized constructor)
> It is a constructor which does not take any argument. It is used to initialize the instance variables to default values.

2. Parameterized Constructor
> It is a constructor which takes arguments. It is used to initialize the instance variables to the values passed as arguments.

'''

# class Employee:
#     def __init__(self):
#         self.name = None
#         self.department = "IT"
#         self.pay = 0

#     def display(self):
#         print("Name: ", self.name)
#         print("Department: ", self.department)
#         print("Pay: ", self.pay)

# emp1 = Employee() # constructor is called automatically when an object is created   

# emp1.name = input("Enter name: ")
# emp1.pay = int(input("Enter pay: "))

# emp1.display()



# parameterized constructor
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Roll: ", self.roll)
        print("Marks: ", self.marks)

s1 = Student("Shrey", 420, 69)  # constructor is called automatically when an object is created
s2 = Student("Shreya", 421, 70) 
s1.display()
s2.display()

"""
Task:

Create a class called Employee with the following attributes:
1. name
2. department
3. pay
4. email

Create a parameterized constructor to initialize the instance variables.
Create a method called display() to display the details of the employee.
Create two objects of the class Employee and display the details of the employees.

"""

