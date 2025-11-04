import array as ar


class RemoveElementArray:
    def __init__(self):
        self.numbers = ar.array("i", [])

    def fill_array(self):
        amount_numbers = int(input("How many numbers do you want to enter: "))
        for i in range(amount_numbers):
            number = int(input(f"Enter {i + 1} number: "))
            self.numbers.append(number)

    def remove_element(self):
        remove_element = int(input("What element do you want to remove: "))
        self.numbers.remove(remove_element)

    def remove_position_element(self):
        remove_position = int(input("What position of element do you want to remove: "))
        if 0 <= remove_position < len(self.numbers):
            self.numbers.pop(remove_position)
        else:
            print("You entered wrong position!")

    def display_arrays(self):
        print(f"Array: {self.numbers}")


if __name__ == "__main__":
    numbers = RemoveElementArray()
    numbers.fill_array()
    numbers.display_arrays()
    numbers.remove_element()
    numbers.display_arrays()
    numbers.remove_position_element()
    numbers.display_arrays()
