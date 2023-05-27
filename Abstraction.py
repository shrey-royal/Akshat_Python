"""
Abstraction is the process of hiding the implementation details and showing only the functionality to the user.

In python, we use abstract classes and interfaces to achieve abstraction. Python does not have interfaces, but it has abstract classes.

An abstract class is a class that generally provides incomplete functionality and contains one or more abstract methods. Abstract methods are the methods that generally don't have any implementation, it is left to the sub classes to provide implementation for the abstract methods.

We can create an abstract class by inheriting from the abc module. The abc module provides the base for defining Abstract Base classes(ABC) in python. ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.

Access Modifiers in Python:
Access modifiers are used to restrict the access of a class, constructor, data member and method in another class. 

In python, there are three types of access modifiers:

Public Access Modifier: The members of a class that are declared public are easily accessible from any part of the program. All data members and member functions of a class are public by default.

Protected Access Modifier: The members of a class that are declared protected are only accessible to a class derived from it. Data members of a class are declared protected by adding a single underscore '_' symbol before the data member of that class.

Private Access Modifier: The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier. Data members of a class are declared private by adding a double underscore '__' symbol before the data member of that class.

private-> __variable -> scope: within the class
protected-> _variable -> scope: within the class and subclass
public-> self.variable   -> scope: within the class, subclass and outside the class


"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
square = Square(5)
print(square.area())
print(square.perimeter())

rectangle = Rectangle(2, 4)
print(rectangle.area())
print(rectangle.perimeter())