class Constructor_Non_parametrized:
    def __init__(self):
        print("Non parametrized constructor!")


class Constructor_parametrized:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Destructor:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created!")

    def __del__(self):
        print(f"{self.name} deleted!")


Constructor_Non_parametrized()

param_constructor = Constructor_parametrized("Ser", 19)
print(
    f"Parametrized constructor: User - {param_constructor.name}, age - {param_constructor.age}"
)

destructor = Destructor("Mike")

del destructor
