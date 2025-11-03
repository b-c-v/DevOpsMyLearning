import array as ar


class OddEvenArray:
    def __init__(self):
        self.numbers = ar.array("i", [])
        self.odd_array = ar.array("i", [])
        self.even_array = ar.array("i", [])

    def fill_array(self):
        amount_numbers = int(input("How many numbers do you want to enter: "))
        for i in range(amount_numbers):
            number = int(input(f"Enter {i + 1} number: "))
            self.numbers.append(number)

    def separate_odd_even_numbers(self):
        for i in self.numbers:
            if i % 2 == 0:
                self.even_array.append(i)
            else:
                self.odd_array.append(i)

    def display_arrays(self):
        print(f"Odd numbers: {self.odd_array}")
        print(f"Even numbers: {self.even_array}")


if __name__ == "__main__":
    numbers = OddEvenArray()
    numbers.fill_array()
    numbers.separate_odd_even_numbers()
    numbers.display_arrays()
