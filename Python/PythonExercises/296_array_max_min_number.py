import array as ar


class MaxMinNumberArray:
    def __init__(self):
        self.numbers = ar.array("i", [])

    def fill_array(self):
        amount_numbers = int(input("How many numbers do you want to enter: "))
        for i in range(amount_numbers):
            number = int(input(f"Enter {i + 1} number: "))
            self.numbers.append(number)

    def min_max_number(self):
        max_number = self.numbers[0]
        min_number = self.numbers[0]

        for i in self.numbers:
            if max_number < i:
                max_number = i
            elif min_number > i:
                min_number = i
        print(f"The biggest number is {max_number}")
        print(f"The smallest number is {min_number}")

    def display_array(self):
        print(f"Array: {self.numbers}")


if __name__ == "__main__":
    numbers = MaxMinNumberArray()
    numbers.fill_array()
    numbers.min_max_number()
