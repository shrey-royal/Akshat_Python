"""
private-> __variable -> scope: within the class
protected-> _variable -> scope: within the class and subclass
public-> self.variable   -> scope: within the class, subclass and outside the class
"""


# public Access Modifier
"""
class Planets:

    def __init__(self, nameOfPlanet, distanceFromSun, mass, radius, gravity, numberOfMoons):
        self.nameOfPlanet = nameOfPlanet
        self.distanceFromSun = distanceFromSun
        self.mass = mass
        self.radius = radius
        self.gravity = gravity
        self.numberOfMoons = numberOfMoons

    def printData(self):
        print("Name of the planet: ", self.nameOfPlanet)
        print("Distance from sun: ", self.distanceFromSun)
        print("Mass: ", self.mass)
        print("Radius: ", self.radius)
        print("Gravity: ", self.gravity)
        print("Number of moons: ", self.numberOfMoons)

planets = Planets("Earth", "149.6 million km", "5.972 × 10^24 kg", "6,371 km", "9.807 m/s²", "1")
planets.printData()
"""

"""
# protected Access Modifier

class Planets:
    
        def __init__(self, nameOfPlanet, distanceFromSun, mass, radius, gravity, numberOfMoons):
            self._nameOfPlanet = nameOfPlanet
            self._distanceFromSun = distanceFromSun
            self._mass = mass
            self._radius = radius
            self._gravity = gravity
            self._numberOfMoons = numberOfMoons
            # print("id: ", id(self._nameOfPlanet))

class PlanetsData(Planets):
        
        def __init__(self, nameOfPlanet, distanceFromSun, mass, radius, gravity, numberOfMoons):
            super().__init__(nameOfPlanet, distanceFromSun, mass, radius, gravity, numberOfMoons)
            
        def printData(self):
            print("Name of the planet: ", self._nameOfPlanet)
            print("Distance from sun: ", self._distanceFromSun)
            print("Mass: ", self._mass)
            print("Radius: ", self._radius)
            print("Gravity: ", self._gravity)
            print("Number of moons: ", self._numberOfMoons)
            # print("id: ", id(self._nameOfPlanet))
    
planetsData = PlanetsData("Earth", "149.6 million km", "5.972 × 10^24 kg", "6,371 km", "9.807 m/s²", "1")
planetsData.printData()
"""        
# private Access Modifier

# program to illustrate private access modifier in a class

class Geek:
	
	# private members
	__name = None
	__roll = None
	__branch = None

	# constructor
	def __init__(self, name, roll, branch):
		self.__name = name
		self.__roll = roll
		self.__branch = branch

	# private member function
	def __displayDetails(self):
		
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	# public member function
	def accessPrivateFunction(self):
			
		# accessing private member function
		self.__displayDetails()

# creating object
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()
