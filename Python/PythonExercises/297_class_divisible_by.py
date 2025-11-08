class DivisibleBy:
    def input_number(self):
        self.user_number = int(input("Enter any number: "))
        self.divisible_number = int(input("Enter a divisor: "))

    def check_is_divisible(self):
        if self.user_number % self.divisible_number == 0:
            print(
                f"The number {self.user_number} is divisible by {self.divisible_number}!"
            )
        else:
            print(
                f"The number {self.user_number} is not divisible by {self.divisible_number}!"
            )


if __name__ == "__main__":
    numbers = DivisibleBy()
    numbers.input_number()
    numbers.check_is_divisible()
