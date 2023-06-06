# Data Encapsulation: Data Encapsulation is defined as the wrapping up of data under a single unit. It is the mechanism that binds together code and the data it manipulates.Other way to think about encapsulation is, it is a protective shield that prevents the data from being accessed by the code outside this shield.

class Person: # data is wrapped up in a class
    __name = None # private variable
    __age = None # private variable
    __gender = None # private variable

    #getter method to get the value of private variable
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def getGender(self):
        return self.__gender
    
    #setter method to set the value of private variable
    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setGender(self, gender):
        self.__gender = gender

    # printing details of the person
    def printDetails(self):
        # print(id(self.__name))
        print("Printing details of the person")
        print("Name: ", self.__name)
        print("Age: ", self.__age)
        print("Gender: ", self.__gender)

# Person = Person() # creating object of the class
# Person.__name = "John" # accessing private variable
# print(Person.__name) # printing private variable
# print(id(Person.__name)) # printing id of the private variable
# Person.printDetails() # calling printDetails() method of the class

people = Person() # creating object of the class

people.setName("John") # calling setter method to set the value of private variable
people.setAge(25)
people.setGender("Male")

print(people.getName()) # calling getter method to get the value of private variable
print(people.getAge())
print(people.getGender())

people.printDetails() # calling printDetails() method of the class