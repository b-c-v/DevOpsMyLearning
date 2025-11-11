# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# Create a Class. To create a class, use the keyword "class":
class MyClass:
    x = 5


# Create Object. We can use the class named MyClass to create objects:
# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)  # 5


# ***The __init__() constructor method.***
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


# ***The __new__() method***
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

# ***The __str__() method***
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


# ***__del__***
# __del__ is a destructor method is used to define the actions that should be performed before an object is destroyed. This can include releasing external resources such as files or database connections associated with the object.
# If a class does not implement __del__, Python relies solely on its automatic garbage collector to reclaim memory.
class SimpleObject:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"SimpleObject '{self.name}' is being destroyed.")


obj = SimpleObject("A")
del obj  # SimpleObject 'A' is being destroyed

# ***Object Methods.***
# Objects can also contain methods. Methods in objects are methods that belong to the object.
# Insert a method that prints a greeting, and execute it on the p1 object:
# Note: The "self" parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()  # Hello my name is John


# ***"self" parameter***
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
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

# ***Modify Object Properties.***
# Set the age of p1 to 40:
p1.age = 40


# ***Delete Object Properties.***
# You can delete properties on objects by using the del keyword:
# Delete the age property from the p1 object:
del p1.age

# ***Delete Objects.***
# You can delete objects by using the del keyword:
# Delete the p1 object:
del p1


# ***Class variables, instance variables and local variables***
"""
Class variables are shared by all instances of a class.
Instance variables are unique to each object and are usually defined inside methods (commonly inside __init__()).
Local variables are defined within a method and exist only while that method executes.
"""


class Variables:
    class_variable = 10  # Class variable: shared among all instances of the class

    def __init__(self):
        self.instance_variable_init = 20  # Instance variable: unique to each instance

    def my_fun(self):
        local_variable = (
            30  # Local variable: only exists during this method's execution
        )
        print(f"Local variable inside method: {local_variable}")
        # Instance variable created inside a method: only exists after this method is called
        self.instance_variable_function = 40


myobj = Variables()
print(f"Class variable: {myobj.class_variable}")  # 10
# print(myobj.local_variable)  # Error: local variable, exists only during method execution and cannot be accessed outside the method
# print(myobj.instance_variable_function)  # Error: instance variable, created only when the method my_fun() is executed
myobj.my_fun()
print(
    f"Instance variable in the function: {myobj.instance_variable_function}"
)  # 40 Now exists for this instance

# Class variables are stored at the class level - all instances reference the same memory location.
myobj2 = Variables()
print(f"Before modification myobj.class_variable: {myobj.class_variable}")  # 10
print(f"Before modification myobj2.class_variable: {myobj2.class_variable}")  # 10

# Class variables can be modified via ClassName.var and changes affect all instances
Variables.class_variable = 50
print(f"After modifying myobj.class_variable: {myobj.class_variable}")  # 50
print(f"After modifying myobj2.class_variable: {myobj2.class_variable}")  # 50

# Instance variables are unique per object; modifying the class attribute with the same name does not affect existing instances
Variables.instance_variable_init = 60
print(f"myobj.instance_variable_init: {myobj.instance_variable_init}")  # 20
print(f"myobj2.instance_variable_init: {myobj2.instance_variable_init}")  # 20
# Individual instance modification
myobj.instance_variable_init = 70
print(f"myobj.instance_variable_init: {myobj.instance_variable_init}")  # 70
print(f"myobj2.instance_variable_init: {myobj2.instance_variable_init}")  # 20


# ***The "pass" Statement***
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.


class Person:
    pass


# ***Access modifiers: Public, Protected and Private***
# Access modifiers control how class attributes and methods can be accessed. Python uses naming conventions based on underscores to signal intended access levels rather than enforce them.
"""
Public Members:
    - no leading underscore in the name
    - accessible from anywhere.
    - default access level in Python

Protected Members: 
    - prefixed with a single underscore (_)
    - intended for internal use within the class and subclasses
    - still accessible externally if explicitly referenced

Private Members: 
    - prefixed with double underscores (__)
    - accessible only within the defining class
    - internally renamed to _ClassName__attributeName
"""


class Person:
    def __init__(self):
        self.public = "public variable"
        self._protected = "protected variable"
        self.__private = "private variable"

    def public_function(self):
        print(f"This is a public function and contains {self.public}!")

    def _protected_function(self):
        print(f"This is a protected function and contains {self._protected}!")

    def __private_function(self):
        print(f"This is a private function and contains {self.__private}!")

    # Internal method to access private function safely
    def access_private_function(self):
        self.__private_function()


class Student(Person):
    def show_info(self):
        print(f"Student inherits: {self.public}")
        print(f"Student inherits: {self._protected}")
        # print(f"Student inherit: {self.__private}") # Raise an AttributeError


# Create an instance of Person
person = Person()
print(f"Person: {person.public}")
print(f"Person: {person._protected}")  # not recommended
# print(f"Person: {person.__private}") # Raise an AttributeError
print(
    f"Person: {person._Person__private}"
)  # Access via name mangling (not recommended)
person.public_function()
person._protected_function()  # not recommended
# person.__private_function() # Raise an AttributeError
person._Person__private_function()  # Access via name mangling (not recommended)
person.access_private_function()

# Create an instance of Student (inherits from Person)
student = Student()
print(f"Student: {student.public}")
print(f"Student: {student._protected}")  # not recommended
# print(f"Student: {student.__private}") # Raise an AttributeError
print(
    f"Student: {student._Person__private}"
)  # Access via name mangling (not recommended)
student.show_info()
student.public_function()
student._protected_function()
# student.__private_function() # Raise an AttributeError
student._Person__private_function()  # Access via name mangling (not recommended)
student.access_private_function()
