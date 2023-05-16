'''
Multi-level Inheritance:
    - one parent class which is inherited by another child class and that child class is inherited by another child class

'''

class Animal:
    # class attributes
    noOfLegs = None
    # is it carnivorous or herbivorous or omnivorous
    type = None

    def __init__(self, noOfLegs, type):
        self.noOfLegs = noOfLegs
        self.type = type

    def printAnimal(self):
        print("Animal has {} legs and it is {}".format(self.noOfLegs, self.type))

class Dog(Animal):
    # class attributes
    name = None
    age = None

    def __init__(self, noOfLegs, type, name, age):
        super().__init__(noOfLegs, type)
        self.name = name
        self.age = age

    def printDog(self):
        print("Dog has {} legs and it is {}".format(self.noOfLegs, self.type))
        print("Dog's name is {} and it is {} years old".format(self.name, self.age))

class Puppy(Dog):
    # class attributes
    color = None
    breed = None

    def __init__(self, noOfLegs, type, name, age, color, breed):
        super().__init__(noOfLegs, type, name, age)
        self.color = color
        self.breed = breed

    def printPuppy(self):
        print("Puppy has {} legs and it is {}".format(self.noOfLegs, self.type))
        print("Puppy's name is {} and it is {} years old".format(self.name, self.age))
        print("Puppy's color is {} and it is {}".format(self.color, self.breed))

# creating object of Puppy class
puppy = Puppy(4, "carnivorous", "Tommy", 2, "brown", "German Shepherd")

# calling printAnimal() method of Animal class
puppy.printAnimal()

# calling printDog() method of Dog class
puppy.printDog()

# calling printPuppy() method of Puppy class
puppy.printPuppy()