class MinMaxNumber:
    def __init__(self):
        self.number_list = []

    def get_numbers(self):
        amount_numbers = int(input("How many numbers do you want to enter: "))

        for i in range(amount_numbers):
            number = int(input(f"Enter your {i+1} number: "))
            self.number_list.append(number)

    def find_min_max(self):
        print(f"The biggest number is {max(self.number_list)}")
        print(f"The smallest number is {min(self.number_list)}")

if __name__ == "__main__":
    numbers = MinMaxNumber()
    numbers.get_numbers()
    numbers.find_min_max()
