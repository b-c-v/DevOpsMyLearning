class DivisibleBy:
    def get_number(self):
        self.user_number = int(input("Enter any number: "))
        self.divisor_number_1 = int(input("Enter first divisor: "))
        self.divisor_number_2 = int(input("Enter second divisor: "))

    def check_is_divisible(self):
        if (
            self.user_number % self.divisor_number_1 == 0
            and self.user_number % self.divisor_number_2 == 0
        ):
            print(
                f"The number {self.user_number} is divisible by {self.divisor_number_1} and {self.divisor_number_2}!"
            )
        else:
            print(
                f"The number {self.user_number} is not divisible by {self.divisor_number_1} and {self.divisor_number_2}!"
            )


if __name__ == "__main__":
    numbers = DivisibleBy()
    numbers.get_number()
    numbers.check_is_divisible()
