# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# ***Function Polymorphism***
# An example of a Python function that can be used on different objects is the len() function.

# For strings len() returns the number of characters:
x = "Hello World!"
print(len(x)) # 12

# For tuples len() returns the number of items in the tuple:
mytuple = ("apple", "banana", "cherry")
print(len(mytuple)) # 3

# For dictionaries len() returns the number of key/value pairs in the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "fuel": "patrol"
}
print(len(thisdict)) # 4


# ***Class Polymorphism***
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

# Different classes with the same method:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!", end = ' ')

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!", end = ' ')

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

# Because of polymorphism we can execute the same method for all three classes.
for x in (car1, boat1, plane1):
  x.move() # Drive! Sail! Fly!


# ***Inheritance Class Polymorphism***
# Child classes inherits the properties and methods from the parent class.
# Because of polymorphism we can execute the same method for all classes.
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

# the Car class is empty, but it inherits brand, model, and move() from Vehicle.
class Car(Vehicle):
  pass

# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.
class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand, end = ' ')
  print(x.model, end = ' ')
  x.move()
