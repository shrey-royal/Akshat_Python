# class Car:
#     def start(self):
#         print("Car Started")

#     def stop(self):
#         print("Car Stopped")

# c = Car()

# c.start()
# c.stop()

# Self is a keyword which is used to refer to the current instance of the class.

# class Employee():
#     def scanEmployeeDetails(self):
#         self.first = input("Enter the first name of the employee: ")
#         self.last = input("Enter the last name of the employee: ")
#         self.email = input("Enter the email of the employee: ")
#         self.salary = int(input("Enter the salary of the employee: "))
#         self.age = int(input("Enter the age of the employee: "))
#         self.department = input("Enter the department of the employee: ")
#         self.designation = input("Enter the designation of the employee: ")

#     def printEmployeeDetails(self):
#         print(f"First Name: {self.first}\nLast Name: {self.last}\nEmail: {self.email}\nSalary: {self.salary}\nAge: {self.age}\nDepartment: {self.department}\nDesignation: {self.designation}")


# e = Employee()

# e.scanEmployeeDetails()
# e.printEmployeeDetails()

"""
Tasks: 

1. Create a class Car with attributes like model, color, company, etc. and methods like start, stop, accelerate, etc. Create 5 different objects of this class and call the methods using the objects.
    > methods: start, stop, accelerate, etc.
    > attributes: model, color, company, etc.


"""

# class Car:
#     model = None
#     color = None
#     company = None

#     def start(self):
#         print("Car Started")

#     def stop(self):
#         print("Car Stopped")

#     def accelerate(self):
#         print("Car Accelerated")

#     def setCarDetails(self):
#         self.model = input("Enter the model of the car: ")
#         self.color = input("Enter the color of the car: ")
#         self.company = input("Enter the company of the car: ")


#     def getCarDetails(self):
#         print(f"Car Details:\nModel: {self.model}\nColor: {self.color}\nCompany: {self.company}")
        

# c = Car()

# c.setCarDetails()

# c.start()
# c.accelerate()
# c.stop()

# c.getCarDetails()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Student:
    name = None
    grade = None
    subjects = []

    def setStudentDetails(self):
        self.name = input("Enter the name of the student: ")
        self.grade = int(input("Enter the grade of the student: "))
        self.subjects = input("Enter the subjects of the student: ").split()

    def getStudentDetails(self):
        print(f"Student Details:\nName: {self.name}\nGrade: {self.grade}\nSubjects: {self.subjects}")

    def searchStudentbyName(self, name):
        if self.name == name:
            self.getStudentDetails()
        

s = []

for i in range(3):
    obj = Student()
    obj.setStudentDetails()
    s.append(obj)

for i in s:
    i.getStudentDetails()


name = input("Enter the name of the student to search: ")
for i in s:
    print(i.searchStudentbyName(name))



"""
Task: 

create a class House with attributes like color, number of rooms, number of bathrooms, etc. and methods like setHouseDetails, getHouseDetails, searchHouseByColor. Create 5 different objects of this class and call the methods using the objects.

"""