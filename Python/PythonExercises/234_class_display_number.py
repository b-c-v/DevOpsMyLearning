class MultiplyTable:
    def get_number(self):
        self.number = int(input("Enter your number: "))

    def display_table(self):
        print(f"Multiply table of number {self.number}: ")
        for i in range(1, 10):
            print(f"{self.number} * {i} = {self.number * i}")


obj = MultiplyTable()
obj.get_number()
obj.display_table()
