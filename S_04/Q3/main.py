from geometry import Shape, ShapeList, Circle, Rectangle, Square, Triangle, Equilateral_triangle, Regular_pantagon
from os import system

text = """
Learn Geometry.
  What do you want to do?
  (1) Add new shape
  (2) Show all shapes
  (3) Show shape with the largest perimeter
  (4) Show shape with the largest area
  (5) Show formulas
  (0) Exit program
  """
if __name__ == "__main__":
    command = None
    all_g = ShapeList()

    while command != "0":
        if command == "1":
            system("cls")
            print("enter the Shape type: "
                  "\n (1) Circle"
                  "\n (2) Triangle"
                  "\n (3) Equilateral triangle"
                  "\n (4) Rectangle"
                  "\n (5) Square"
                  "\n (6) Regular pentagon")
            shape_type = input()
            if shape_type == "1":
                system("cls")
                data = float(input("please enter information of shape. (Radius >= 0)(Example: 5)"))
                Shape.check_if_args_not_below_zero(data)
                all_g.add_shape(Circle(data))

            if shape_type == "2":
                system("cls")
                data = list(map(float
                                , input("please enter information of shape. (a, b, c >= 0)(Example: 3 4 5)").split()))
                Shape.check_if_args_not_below_zero(*data)
                all_g.add_shape(Triangle(*data))

            if shape_type == "3":
                system("cls")
                data = float(input("please enter information of shape. (a >= 0)(Example: 5)"))
                Shape.check_if_args_not_below_zero(data)
                all_g.add_shape(Equilateral_triangle(data))

            if shape_type == "4":
                system("cls")
                data = list(map(float, input("please enter information of shape. (a, b >= 0)(Example: 5 10)").split()))
                Shape.check_if_args_not_below_zero(*data)
                all_g.add_shape(Rectangle(*data))

            if shape_type == "5":
                system("cls")
                data = float(input("please enter information of shape. (a >= 0)(Example: 5)"))
                Shape.check_if_args_not_below_zero(data)
                all_g.add_shape(Square(data))

            if shape_type == "6":
                system("cls")
                data = float(input("please enter information of shape. (a >= 0)(Example: 5)"))
                Shape.check_if_args_not_below_zero(data)
                all_g.add_shape(Regular_pantagon(data))

        if command == "2":
            system("cls")
            all_g.get_shapes_table()
            input("\n")

        if command == "3":
            system("cls")
            anw = all_g.get_largest_shape_by_perimeter()
            if anw is None:
                print("there is no shape")
            else:
                print(anw.get_perimeter())
            input()

        if command == "4":
            system("cls")
            anw = all_g.get_largest_shape_by_area()
            if anw is None:
                print("there is no shape")
            else:
                print(anw.get_area())
            input()

        if command == "5":
            system("cls")
            select_shape = input("enter the Shape type: "
                                 "\n (1) Circle"
                                 "\n (2) Triangle"
                                 "\n (3) Equilateral triangle"
                                 "\n (4) Rectangle"
                                 "\n (5) Square"
                                 "\n (6) Regular pentagon")
            if select_shape == "1":
                print("area: ", Circle.area_f, "perimeter: ", Circle.perimeter_f)
            if select_shape == "2":
                print("area: ", Triangle.area_f, "perimeter: ", Triangle.perimeter_f)
            if select_shape == "3":
                print("area: ", Equilateral_triangle.area_f, "perimeter: ", Equilateral_triangle.perimeter_f)
            if select_shape == "4":
                print("area: ", Rectangle.area_f, "perimeter: ", Rectangle.perimeter_f)
            if select_shape == "5":
                print("area: ", Square.area_f, "perimeter: ", Square.perimeter_f)
            if select_shape == "6":
                print("area: ", Regular_pantagon.area_f, "perimeter: ", Regular_pantagon.perimeter_f)
            input()

        system("cls")
        print(text)
        command = input()
