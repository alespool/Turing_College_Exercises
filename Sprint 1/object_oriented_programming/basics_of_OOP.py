# a class is a blueprint, an instance has the particular characteristics of the blueprint
# dog is a class, its name, age, sex etc its attributes and when we create onme such dog its an instance

class Dog:
    # this is a class attribute, which is defined outside the init
    species = "Canis familiaris"

    # The __init__() method initializes/sets the initial state of the objects
    def __init__(self, name, age, breed):
        # we dont need to worry about the self parameters as pthon already processes it
        # these are instance attributes, they are specific to a particular instance
        self.name = name
        self.age = age
        self.breed = breed

    # Dunder methods, they customize classes
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


# customn objects are mutable by default, like lists and dictionaries
miles = Dog("Miles", 4, '')

print(miles)

print(miles.speak("woof woof"))

print(miles.speak("bow bow"))


# Check understanding
# create car with 2 instance attributes: color and mileage

class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

    def speak(self, sound):
        return f"{self.name} says {sound}"

subaru = Car("Blue", 25000)
toyota = Car("Grey", 78000)

# print(subaru, toyota)

print("*"* 25 + " Inherited Classes " + "*" * 25)
# Inheritance is when a cass takes on the attributes and methods of another class like its child
# child classes can ovveride or extend the methods and attribvutes of parents classes

# dog park example
# added breed to previous class

miles = Dog("Miles", 4, "Jack Russel terrier")
buddy = Dog("Buddy", 9, "Dachsund")
jack = Dog("Jack", 3, "bulldog")
jim = Dog("Jim", 5, "Bulldog")

# this is quite inconvenient
# print(buddy.speak("Yap"))
# print(jim.speak("Woof"))

# we can simplify this by making a child dog class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Dachsund(Dog):
    pass
    # def speak(self, sound="Arf"):
    #     return f"{self.name} says {sound}"

class Bulldog(Dog):
    pass
    # def speak(self, sound="Arf"):
    #     return f"{self.name} says {sound}"


miles = JackRussellTerrier("Miles", 4, "Jack Russel terrier")
buddy = Dachsund("Buddy", 9, "Dachsund")
jack = Bulldog("Jack", 3, "bulldog")
jim = Bulldog("Jim", 5, "Bulldog")

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("woof"))

# check if its an instance of Dog
print(isinstance(miles, Dog))
print(isinstance(jack, Dachsund))

# check additional methods we gave to child classes
print(miles.speak("Grr"))
print(miles.speak()) # this remains the one inputted in the child class, as we have overriden it

#changes made to the parent class automatically propagate to the child class
# as long as the method is not overridden in the child class

# I added the def speak method to the parent class
print(jim.speak("Woof"))

class JackRusselTerrier(Dog):
    def speak(self, sound = "Arf"):
        return super().speak(sound) # This connects me to the 'speak' method present in the parent class

miles = JackRusselTerrier("Miles", 4, "Jack Russy")
print(miles.speak())

# check understanding 2
# create golden retriever class based on a dog class

class Dog_1:
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog_1):
    def speak(self, sound = "Bark"):
        return super().speak(sound)

peggie = GoldenRetriever("Peggie", 6)
print(peggie.speak("Hey You!"))