'''
Hierarchical Inheritance: 
    - one parent class and multiple child class
    - class ChildClass(ParentClass1, ParentClass2, ParentClass3, ...)

'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def details(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Dog_Character:
    def __init__(self, color, breed):
        self.color = color
        self.breed = breed
    
    def details(self):
        print("Color:", self.color)
        print("Breed:", self.breed)

class C(Dog, Dog_Character):
    def __init__(self, name, age, color, breed):
        Dog.__init__(self, name, age)
        Dog_Character.__init__(self, color, breed)
    
    def details(self):
        Dog.details(self)
        Dog_Character.details(self)

c = C("Tommy", 2, "Brown", "German Shepherd")
c.details()