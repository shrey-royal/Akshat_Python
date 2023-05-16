'''
Inheritance: Inheritance is a mechanism in which one class acquires the property of another class. It is an important part of object oriented programming. It specifies that the child class acquires all the properties and behaviors of the parent class. It is used to achieve runtime polymorphism.

It helps in code reusability. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

Syntax:

class Subclass (Parentclass1):
class childclass (Parentclass1, Parentclass2, Parentclass3):

in python we have 5 types of inheritance:

1. Single Inheritance -> one parent class and one child class
2. Multiple Inheritance -> one parent class and multiple child class
3. Multilevel Inheritance -> one parent class and child class(child class is also parent class for another child class)
4. Hierarchical Inheritance -> multiple parent class and one child class
5. Hybrid Inheritance -> combination of multiple and multilevel inheritance

'''

# Single Inheritance

# class Animal:
#     def __init__(self, name, age, color, breed):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.breed = breed

#     def eat(self):
#         print(self.name, "is eating")

#     def sleep(self):
#         print(self.name, "is sleeping")

#     def play(self):
#         print(self.name, "is playing")

# class Dog(Animal):
#     def bark(self):
#         print(self.name, "is barking")

#     def details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Color:", self.color)
#         print("Breed:", self.breed)

# d = Dog("Tommy", 2, "Brown", "German Shepherd")

# d.eat()
# d.sleep()
# d.play()
# d.bark()

# d.details()


# getattr() -> returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.

class Gift:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def details(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

gift = Gift("Teddy Bear", 100, 2)

# print(getattr(gift, "name"))
# print(getattr(gift, "price"))
# print(getattr(gift, "quantity"))
# print(getattr(gift, "100"))

# print(getattr(gift, "name", "Not Found"))

# setattr() -> sets the value of the specified attribute of an object. If the attribute does not exist, then it will be created.

setattr(gift, "name", "Cat")
setattr(gift, "price", 200)
setattr(gift, "quantity", 1)

gift.details()


# delattr() -> deletes the specified attribute (property or method) from the specified object.

delattr(gift, "quantity")
gift.details()