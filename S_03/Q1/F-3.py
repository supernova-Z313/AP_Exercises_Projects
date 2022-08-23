# Q3: Simple OOP Calculator
# https://edabit.com/challenge/ta8GBizBNbRGo5iC6
# notes in question
class Calculator:
    def add(self, e1, e2):
        return e1 + e2

    def subtract(self, e1, e2):
        return e1 - e2

    def multiply(self, e1, e2):
        return e1 * e2

    def divide(self, e1, e2):
        return e1 / e2


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(10, 5))
