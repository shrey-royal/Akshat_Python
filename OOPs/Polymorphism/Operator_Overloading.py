"""
In Python operator overloading is done by defining a special method in the class.
For example, if we want to overload the + operator, we will define a method named __add__().

Example 1: Overloading the + Operator

"""
"""
class Point:    # Point class represents a point in 2-D space
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self ,other):
        x = self.x + other.x    # self.x and other.x are the x coordinates of Point objects
        y = self.y + other.y    # self.y and other.y are the y coordinates of Point objects
        return Point(x, y)      # returns a new Point object with x and y coordinates as the sum of the coordinates of the two points
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 + p2)  # prints (3,5)

"""

# we will append 2 characters using the + operator.

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    # Overloading the + operator
    def __add__(self, other):   # this is a built-in method in python for operator overloading
        return self.cont + other.cont

    def __str__(self):        # this is a built-in method used to print the string
        return self.cont
    
a = SpecialString("Hello")
b = SpecialString(" Python")

print(a + b)    # prints HelloPython