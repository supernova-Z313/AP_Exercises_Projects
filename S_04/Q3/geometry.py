from math import pi, sqrt


class Shape:
    def get_area(self):
        return self.erea

    def get_perimeter(self):
        return self.perimeter

    def __str__(self):
        return self.date_str

    @classmethod
    def check_if_args_not_below_zero(cls, *args):
        for i in args:
            if i < 0:
                raise ValueError
        return True

    @classmethod
    def get_area_formula(cls):
        return str(cls._erea)

    @classmethod
    def get_perimeter_formula(cls):
        return str(cls._perimeter)


class Circle(Shape):
    area_f = "R^2 * pi"
    perimeter_f = "2 * R * pi"

    def __init__(self, radian: float = 1):
        self.r = radian
        self.area = (self.r ** 2) * pi
        self.perimeter = 2 * self.r * pi
        self.date_str = f"Circle, r = {self.r}"

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


class Triangle(Shape):
    area_f = "sqrt(s * (s-a) * (s-b) * (s-c)) , s = perimeter/2"
    perimeter_f = "a + b + c"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.perimeter = self.a + self.b + self.c
        self.half_perimeter = self.perimeter/2
        self.area = sqrt(self.half_perimeter * (self.half_perimeter * (self.half_perimeter - self.a)
                                                * (self.half_perimeter - self.b) * (self.half_perimeter - self.c)))
        self.date_str = f"Triangle, {self.a},{self.b},{self.c}"

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


class Equilateral_triangle(Shape):
    area_f = "a * 3"
    perimeter_f = "sqrt(s * (s - a) *3)"

    def __init__(self, a):
        self.a = a
        self.perimeter = self.a * 3
        self.half_perimeter = self.perimeter/2
        self.area = sqrt(self.half_perimeter * (self.half_perimeter - self.a) * 3)
        self.date_str = f"Equilateral triangle, {self.a}"


class Rectangle(Shape):
    area_f = "a * b"
    perimeter_f = "(a + b) * 2"

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.perimeter = (self.a + self.b) * 2
        self.area = self.a * self.b
        self.date_str = f"Rectangle, {self.a}, {self.b}"


class Square(Shape):
    area_f = "a * a"
    perimeter_f = "a * 4"

    def __init__(self, a):
        self.a = a
        self.area = a * a
        self.perimeter = 4 * a
        self.date_str = f"Square, a = {self.a}"


class Regular_pantagon(Shape):
    area_f = "a * a * 5 / 2"
    perimeter_f = "a * 5"

    def __init__(self, a):
        self.a = a
        self.perimeter = self.a * 5
        self.area = self.a * self.perimeter / 2
        self.date_str = f"Regular pentagon, a = {self.a}"


class ShapeList(Shape):
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            raise TypeError

    def get_shapes_table(self):
        print("| idx |   Class  |     __str__     |  Perimeter  |  Formula  |")
        print("|-----|----------|-----------------|-------------|-----------|")
        for ind, i in enumerate(self.shapes):
            print("|{:^5}|{:^10}|{:^17}|{:^13}|{:^11}|".format(ind, str(type(i))[17:-2], i.__str__()
                                                               , round(i.get_perimeter(), 10), round(i.get_area(), 9)))

    def get_largest_shape_by_perimeter(self):
        max_list = []
        for i in self.shapes:
            max_list.append(i.get_perimeter())
        if len(max_list) == 0:
            return None
        else:
            return self.shapes[max_list.index(max(max_list))]

    def get_largest_shape_by_area(self):
        max_list = []
        for i in self.shapes:
            max_list.append(i.get_area())
        if len(max_list) == 0:
            return None
        else:
            return self.shapes[max_list.index(max(max_list))]


if __name__ == "__main__":
    pass
