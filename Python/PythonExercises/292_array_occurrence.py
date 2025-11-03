import array as ar


class OccurrenceArray:
    def __init__(self):
        self.number_array = ar.array("i", [])

    def fill_array(self):
        amount_numbers = int(input("How many numbers do you want to enter: "))
        for i in range(amount_numbers):
            number = int(input(f"Enter {i + 1} number: "))
            self.number_array.append(number)

    def count_occurrence(self):
        self.user_number = int(input("Enter a number to count its occurrences: "))
        self.occurrence_number = self.number_array.count(self.user_number)

    def display_occurrence(self):
        print(f"Number {self.user_number} occurred {self.occurrence_number} times")


if __name__ == "__main__":
    number_array = OccurrenceArray()
    number_array.fill_array()
    number_array.count_occurrence()
    number_array.display_occurrence()
