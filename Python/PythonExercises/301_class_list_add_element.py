# A class to compute the sum of neighboring numbers in a user-provided list.
class NeighborSumCalculator:
    def __init__(self):
        self.numbers = []
        self.neighbor_sums = []

    def get_numbers(self):
        num_count = int(input("Enter how many numbers you want to input: "))

        for i in range(num_count):
            number = int(input(f"Enter your {i+1} number: "))
            self.numbers.append(number)

    def calculate_neighbor_sums(self):
        for i in range(len(self.numbers) - 1):
            new_number = self.numbers[i] + self.numbers[i + 1]
            self.neighbor_sums.append(new_number)

    def display_lists(self):
        print(f"Original numbers: {self.numbers}")
        print(f"Neighbor sums: {self.neighbor_sums}")


if __name__ == "__main__":
    numbers = NeighborSumCalculator()
    numbers.get_numbers()
    numbers.calculate_neighbor_sums()
    numbers.display_lists()
