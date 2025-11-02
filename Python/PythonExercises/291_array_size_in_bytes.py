import array as ar


class SizeArray:
    # Method create an empty array
    def __init__(self):
        self.number_array = ar.array("i", [])

    # Fill array with values
    def fill_array(self):
        amount_numbers = int(input("How many numbers do you want to enter: "))
        for i in range(amount_numbers):
            number = int(input(f"Enter {i + 1} number: "))
            self.number_array.append(number)

    # Print array data
    def display_array(self):
        print(self.number_array)
        print(f"Each item size: {self.number_array.itemsize} bytes.")
        print(
            f"Total array size: {len(self.number_array) * self.number_array.itemsize} bytes."
        )


if __name__ == "__main__":
    number_array = SizeArray()
    number_array.fill_array()
    number_array.display_array()
