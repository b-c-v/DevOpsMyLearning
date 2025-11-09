class AverageCalculation:
    def __init__(self):
        self.number_list = []

    def get_numbers(self):
        self.amount_numbers = int(input("How many numbers do you want to enter: "))
        for i in range(self.amount_numbers):
            number = int(input(f"Enter your {i+1} number: "))
            self.number_list.append(number)

    def calculate_average(self):
        numbers_sum = sum(self.number_list)
        numbers_average = numbers_sum / self.amount_numbers

        print(f"The sum of your numbers is: {numbers_sum}")
        print(f"The average of your numbers is: {numbers_average}")


if __name__ == "__main__":
    numbers = AverageCalculation()
    numbers.get_numbers()
    numbers.calculate_average()
