"""
Polymorphism is an ability (in OOP) to use common interface for multiple form (data types).
Suppose, we need to color a shape, there are multiple shape option (rectangle, square, circle). 
However we could use same method to color any shape. This concept is called Polymorphism.

Polymorphism is based on the greek words Poly (many) and morphism (forms).


Topics to be covered:
    1. Duck Typing -> Python uses concept of Duck Typing, if it looks like a duck, it is a duck. 
    2. Operator Overloading
    3. Method Overloading
    4. Method Overriding

"""

# Example 1: Using Common Interface for Different Data Types
# Here, we are creating a class and defined a method greeting() to greet. 

class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()  #calling the fly method of the class

#instantiate objects
blu = Parrot()  #creating an object
peggy = Penguin()

#passing the object
flying_test(blu)    #Parrot can fly
flying_test(peggy)  #Penguin can't fly