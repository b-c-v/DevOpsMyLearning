# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# Create a Class. To create a class, use the keyword class:
class MyClass:
    x = 5


# Create Object. We can use the class named MyClass to create objects:
# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)  # 5


# The __init__() method.
# All classes have a method called __init__(), which is always executed when the class is being initiated ()
# Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created:
# Create a class named Person, use the __init__() method to assign values for name and age:


class Person:
    # self - see the explanation below
    def __init__(self, name, age):
        self.name = name  # assign to instance attribute
        self.age = age


p1 = Person("John", 36)

print("__init__() method -", p1.name, p1.age)  # John 36


# The __new__() method
# __new__ is a special method in Python that is responsible for creating a new instance of a class.
# __new__() actually returns the object instance. It is a static method by definition and always takes the class (cls) as its first argument.
#  __new__ method is called first to create an instance of class A and then returns the newly created instance. After that, the __init__ method initializes the instance.
class A:
    def __new__(cls):
        print("Creating instance")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print("Initializing instance")


A()  # Creating instance Initializing instance


# Если в классе явно не определён метод __new__, Python автоматически использует стандартную реализацию из базового класса object
# object.__new__. выделяет память и создаёт пустой объект типа B. После успешного создания объекта вызывает __init__
class B:
    def __init__(self):
        print("__init__ without __new__")


B()

# The __str__() method
# The __str__() method controls what should be returned when the class object is represented as a string.
# If the __str__() method is not set, the string representation of the object is returned:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print("__str__() method -", p1)  # John(36)


# __del__ method is used to define the actions that should be performed before an object is destroyed. This can include releasing external resources such as files or database connections associated with the object.
# If a class does not implement __del__, Python relies solely on its automatic garbage collector to reclaim memory.
class SimpleObject:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"SimpleObject '{self.name}' is being destroyed.")


obj = SimpleObject("A")
del obj  # SimpleObject 'A' is being destroyed

# Object Methods. Objects can also contain methods. Methods in objects are methods that belong to the object.
# Insert a method that prints a greeting, and execute it on the p1 object:
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()  # Hello my name is John


# self Parameter. The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any method in the class:
# Use the words mysillyobject and abc instead of self:
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is", abc.name, "I'm", abc.age)


p1 = Person("John", 36)
p1.myfunc()  # Hello my name is  John I'm 36

# Modify Object Properties.
# Set the age of p1 to 40:
p1.age = 40


# Delete Object Properties. You can delete properties on objects by using the del keyword:
# Delete the age property from the p1 object:
del p1.age

# Delete Objects. You can delete objects by using the del keyword:
# Delete the p1 object:
del p1

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.


class Person:
    pass
