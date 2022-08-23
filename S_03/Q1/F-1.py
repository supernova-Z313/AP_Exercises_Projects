# Q1 : Make a circle with OOP
# https://edabit.com/challenge/nC7iHBbN8FEPy2EJ2
# notes in question
class Circle:
    def __init__(self, arg: float):
        from math import pi
        self.PI = pi
        self.radius = arg

    def getArea(self):
        area = (self.radius ** 2) * self.PI
        return area

    def getPerimeter(self):
        perimeter = self.radius * self.PI * 2
        return perimeter


if __name__ == "__main__":
    print("first line: Circle(11).getArea()\nsecond line: Circle(4.44).getPerimeter()")
    print(Circle(11).getArea())
    print(Circle(4.44).getPerimeter())
