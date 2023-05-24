# Hierarchical Inheritance -> one parent class and multiple child class

class Animal:
    # class attributes
    name = None
    age = None
    color = None
    breed = None

    def __init__(self, name, age, color, breed):
        self.name = name    # here self is the object
        self.age = age
        self.color = color
        self.breed = breed

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")

    def play(self):
        print(self.name, "is playing")


class Dog(Animal):
    type = "Dog"

    def bark(self):
        print(self.name, "is a", self.type, "and he/she is barking.")

class Cat(Animal):
    type = "Cat"

    def meow(self):
        print(self.name, "is a", self.type, "and he/she is meowing.")

class Tiger(Animal):
    type = "Tiger"

    def roar(self):
        print(self.name, "is a", self.type, "and he/she is roaring.")


d = Dog("Tommy", 2, "Brown", "German Shepherd")
# print(d.name, d.age, d.color, d.breed, d.type)
d.abc = "xyz" # adding new attribute to the object
d.eat()
d.sleep()
d.play()
d.bark()

c = Cat("Kitty", 1, "White", "Persian")
# print(c.name, c.age, c.color, c.breed, c.type)
c.eat()
c.sleep()
c.play()
c.meow()

t = Tiger("Sheru", 3, "Yellow", "Bengal")
# print(t.name, t.age, t.color, t.breed, t.type)
t.eat()
t.sleep()
t.play()
t.roar()


# animal = Animal("Tommy", 2, "Brown", "German Shepherd")
# animal.type = "Dog" # adding new attribute to the object
# print(animal.name, animal.age, animal.color, animal.breed, animal.type)