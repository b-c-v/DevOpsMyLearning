import array as ar


class ReverseArray:
    def __init__(self):
        self.numbers = ar.array("i", [])

    def fill_array(self):
        amount_numbers = int(input("How many numbers do you want to enter: "))
        for i in range(amount_numbers):
            number = int(input(f"Enter {i + 1} number: "))
            self.numbers.append(number)

    def reverse_array(self):
        self.numbers.reverse()

    def display_array(self):
        print(f"Array: {self.numbers}")


if __name__ == "__main__":
    numbers = ReverseArray()
    numbers.fill_array()
    numbers.display_array()
    numbers.reverse_array()
    numbers.display_array()
