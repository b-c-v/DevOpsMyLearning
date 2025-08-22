class Student:
    def __init__(self):
        self.name = None
        self.id = None

    def get_data(self):
        self.name = input("Please enter your name: ")
        self.id = int(input("Please enter your ID: "))

    def __str__(self):
        return f"Your name is {self.name} and your ID is {self.id}"


student = Student()
student.get_data()
print(student)


# inheritance
class Worker(Student):
    def __init__(self):
        super().__init__()
        self.graduation_year = None

    def get_data(self):
        super().get_data()
        self.graduation_year = int(input("Please enter year of your graduation: "))

    def __str__(self):
        return f"Your name is {self.name} and your ID is {self.id}, and your graduation year is {self.graduation_year}"


worker = Worker()
worker.get_data()
print(worker)
