"""
# Classes and Objects
Class -> A class is a blueprint for the object.

A Class contains the following:
1. Attributes -> Attributes are the variables that are defined inside the class.
2. Methods -> Methods are the functions that are defined inside the class.

Object -> An object is an instance of a class.
Initializing an object -> Initializing an object means creating an object of a class.
Instantiating a class -> Instantiating a class means creating an object of a class.

# Creating a class

class ClassName:
    # Class body

# Creating an object

objectName = ClassName()    # Instantiating a class


"""

# class Employee:
#     pass
    # first = "Akshat"    # if i write any attribute here, then for all the objects of this class, this attribute will be same

# emp_1 = Employee()  # Instantiating a class

# print(emp_1)    # prints the memory location of the object
# print(f"emp_1 is at : {hex(id(emp_1))}")

# add attributes to the object
# emp_1.first = "Akshat"  # first is an attribute of the object emp_1
# print(emp_1.first)  # prints None
# emp_1.last = "Chaturvedi"
# emp_1.email = "achatur@gmail.com"
# emp_1.pay = 500000, "INR"
# emp_1.age = 20
# emp_1.department = "IT"
# emp_1.designation = "Software Engineer"

# print(f"emp_1.first = {emp_1.first}\nemp_1.last = {emp_1.last}\nemp_1.email = {emp_1.email}\nemp_1.pay = {emp_1.pay}\nemp_1.age = {emp_1.age}\nemp_1.department = {emp_1.department}\nemp_1.designation = {emp_1.designation}")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Student:
    roll_no = None
    name = None
    age = None
    marks = None
    standard = None
    section = None
    gender = None
    fees = None

s = Student()

s.roll_no = int(input("Enter the roll number of the student: "))
s.name = input("Enter the name of the student: ")
s.age = int(input("Enter the age of the student: "))
s.marks = int(input("Enter the marks of the student: "))
s.standard = int(input("Enter the standard of the student: "))
s.section = input("Enter the section of the student: ")
s.gender = input("Enter the gender of the student: ")
s.fees = int(input("Enter the fees of the student: "))

print("Student Details:")

print(f"Roll Number: {s.roll_no}")
print(f"Name: {s.name}")
print(f"Age: {s.age}")
print(f"Marks: {s.marks}")
print(f"Standard: {s.standard}")
print(f"Section: {s.section}")
print(f"Gender: {s.gender}")
print(f"Fees: {s.fees}")


"""
Tasks to be done:

1. Create a class named 'Student' with the following attributes:
    1. roll_no
    2. name
    3. age
    4. marks
    5. standard
    6. section
    
Scan all the details of the student and print them in tabular format like below example:

Student Details:

----------------------------------------------------------
Roll Number   Name    Age    Marks    Standard    Section
----------------------------------------------------------
1             Akshat  20     100      12          A
----------------------------------------------------------
2             Ramesh  17     67       11          B
----------------------------------------------------------
3             Suresh  16     45       11          D
----------------------------------------------------------
4             Sonu    20     78       12          B
----------------------------------------------------------
5             Monu    15     56       12          C

2. Create a class named 'Employee' with the following attributes:
    1. emp_id
    2. name
    3. age
    4. salary
    5. designation
    6. department

Scan all the details of the employee and print them in tabular format like below example:

Employee Details:

------------------------------------------------------------
Emp ID   Name    Age    Salary    Designation    Department
------------------------------------------------------------
1        Akshat  20     100000    Software Engineer    IT
------------------------------------------------------------
2        Ramesh  17     67000     Software Engineer    IT
------------------------------------------------------------
3        Suresh  16     45000     Software Engineer    IT
------------------------------------------------------------
4        Sonu    20     78000     Software Engineer    IT
------------------------------------------------------------
5        Monu    15     56000     Software Engineer    IT


"""