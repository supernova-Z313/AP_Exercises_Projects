
class Integer:
    def __init__(self, val):
        if isinstance(val, int):
            self.value = val
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value)
        elif isinstance(other, Complex):
            # print(self.value)
            # print(other.value)
            return Complex(other.first_part, other.second_part + self.value)
        elif isinstance(other, Matrix):
            return other + self
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value * other.value)
        elif isinstance(other, Complex):
            return Complex(self.value * other.first_part, self.value * other.second_part)
        elif isinstance(other, Matrix):
            mat = []
            for i in other.matrix:
                for j in i:
                    mat.append((j * self).value)
            return Matrix(other.row, other.column, mat)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Integer):
            return self + (other * Integer(-1))
        elif isinstance(other, Complex):
            return Complex(other.first_part, (self.value * -1) + other.second_part)
        else:
            raise TypeError


class Complex:
    def __init__(self, val1: int, val2: int):
        self.first_part = val1
        self.second_part = val2
        if self.first_part == 0 and self.second_part == 0:
            self.value = f"0"
        elif self.first_part == 0:
            self.value = f"{val2}"
        elif self.second_part == 0:
            self.value = f"{val1}i"
        else:
            self.value = f"{val1}i+{val2}"

    def __add__(self, other):
        if isinstance(other, Integer):
            return Complex(self.first_part, self.second_part + other.value)
        elif isinstance(other, Complex):
            return Complex(self.first_part + other.first_part, self.second_part + self.second_part)
        elif isinstance(other, Matrix):
            return other + self
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Integer):
            first = self.first_part * other.value
            second = self.second_part * other.value
            if isinstance(first, str):
                first = 0
            if isinstance(second, str):
                second = 0
            return Complex(first, second)
        elif isinstance(other, Complex):
            return Complex((self.second_part * other.first_part)+(self.first_part * other.second_part),
                           (self.second_part * other.second_part)-(self.first_part * other.first_part))
        elif isinstance(other, Matrix):
            mat = []
            for i in other.matrix:
                for j in i:
                    mat.append((j * self).value)
            return Matrix(other.row, other.column, mat)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Integer):
            return Complex(self.first_part, self.second_part + (Integer(-1) * other))
        elif isinstance(other, Complex):
            return Complex(self.first_part - other.first_part, self.second_part - other.second_part)
        else:
            raise TypeError


class Matrix:
    def __init__(self, row: int, column: int, mat: list):
        self.row = row
        self.column = column
        self.matrix = []
        little_list = []
        for ind, i in enumerate(mat, start=1):
            if isinstance(i, int):
                little_list.append(Integer(i))
            else:
                if "i+" in i:
                    i = i.split("i+")
                    little_list.append(Complex(int(i[0]), int(i[1])))
                elif "i" in i:
                    i = i.split("i")
                    little_list.append(Complex(int(i[0]), 0))
                elif i == "0":
                    little_list.append(Complex(0, 0))
                else:
                    little_list.append(Complex(0, int(i)))
            if ind % row == 0:
                self.matrix.append(little_list.copy())
                little_list.clear()

    def make_matrix_from_string(self, elements: str):
        list_of_row = elements.split(",")
        mat = []
        for i in list_of_row:
            mat.append(i.split(" "))
        matrix = []
        for i in mat:
            for j in i:
                try:
                    matrix.append(int(j))
                except:
                    matrix.append(j)
        con = elements.count(",")+1
        return Matrix(len(matrix)//con, con, matrix)

    @staticmethod
    def make_unit_matrix(n):
        mat = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    mat.append(1)
                else:
                    mat.append(0)
        return Matrix(n, n, mat)

    @staticmethod
    def get_ith_row(matrix, i: int):
        return matrix.matrix[i]

    @staticmethod
    def get_ith_col(matrix, i: int):
        mat = []
        for j in matrix.matrix:
            mat.append(j[i])
        return mat

    @staticmethod
    def is_zero_matrix(matrix):
        all_c = matrix.row * matrix.column
        counter = 0
        for i in matrix.matrix:
            for j in i:
                if j.value == 0:
                    counter += 1
        return counter == all_c

    @staticmethod
    def is_unit_matrix(matrix):
        if matrix.row == matrix.column:
            ghotr_counter = 0
            baghi = 0
            for ind, i in enumerate(matrix.matrix):
                for inx, j in enumerate(i):
                    if ind == inx:
                        if j.value == 1:
                            ghotr_counter += 1
                    elif j.value == 0:
                        baghi += 1
            return (ghotr_counter == matrix.row) and (baghi == (matrix.row * (matrix.row-1)))
        else:
            return False

    @staticmethod
    def is_top_triangular_matrix(matrix):
        counter = 0
        for ind, i in enumerate(matrix.matrix):
            for inx, j in enumerate(i):
                if ind == 0:
                    pass
                elif inx < ind:
                    if j.value == 0:
                        counter += 1
        return counter == (matrix.row * (matrix.row - 1))//2

    @staticmethod
    def is_bottom_triangular_matrix(matrix):
        counter = 0
        for ind, i in enumerate(matrix.matrix):
            for inx, j in enumerate(i):
                if ind == matrix.row-1:
                    pass
                elif inx > ind:
                    if j.value == 0:
                        counter += 1
        return counter == (matrix.row * (matrix.row - 1))//2

    def __add__(self, other):
        if isinstance(other, Matrix):
            if (other.row == self.row) and (other.column == self.column):
                mat = []
                for ind, i in enumerate(other.matrix):
                    for inx, j in enumerate(i):
                        mat.append((j + self.matrix[ind][inx]).value)
                return Matrix(self.row, self.column, mat)
            else:
                raise ValueError
        elif isinstance(other, Integer) or isinstance(other, Complex):
            mat = []
            for i in self.matrix:
                for j in i:
                    mat.append((j + other).value)
            return Matrix(self.row, self.column, mat)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Integer) or isinstance(other, Complex):
            return other + self
        elif isinstance(other, Matrix):
            if self.row == other.column:
                mat = []
                for i in range(self.column):
                    for j in range(other.row):
                        x = Integer(0)
                        for ind, c in enumerate(self.matrix[i]):
                            for inx, v in enumerate(Matrix.get_ith_col(other, j)):
                                if ind == inx:
                                    x = x + (c * v)
                        mat.append(x.value)
                return Matrix(other.row, self.column, mat)
            else:
                raise ValueError
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Integer):
            mat = []
            for i in self.matrix:
                for j in i:
                    mat.append((other - j).value)
            return Matrix(self.row, self.column, mat)
        elif isinstance(other, Complex):
            mat = []
            for i in self.matrix:
                for j in i:
                    mat.append((other - j).value)
            return Matrix(self.row, self.column, mat)
        elif isinstance(other, Matrix):
            if (self.row == other.row) and (self.column == other.column):
                mat = []
                for ind, i in enumerate(self.matrix):
                    for inx, j in enumerate(i):
                        mat.append((j - other.matrix[ind][inx]).value)
                return Matrix(self.row, self.column, mat)
            else:
                raise ValueError
        else:
            raise TypeError


def multiply(x, y):
    return x * y


if __name__ == "__main__":
    Integer(5)
    s = Matrix(3, 2, [1, 2, 3, 4, "5i+1", 6])
    for i in s.matrix:
        for j in i:
            print(j.value, end=" ")
        print()
    print()

    x = s.make_matrix_from_string("9 8 7,6 5 4,3 2 1")

    for i in x.matrix:
        for j in i:
            print(j.value, end=" ")
        print()

    q = Matrix.make_unit_matrix(3)
    for i in q.matrix:
        for j in i:
            print(j.value, end=" ")
        print()
    print()

    print(Matrix.get_ith_row(q, 1))
    print(Matrix.get_ith_col(q, 1))

    print(Matrix.is_zero_matrix(q))
    f = s.make_matrix_from_string("0 0 0,0 0 0,0 0 0")
    print(Matrix.is_zero_matrix(f))

    print(Matrix.is_unit_matrix(q))
    print(Matrix.is_unit_matrix(f))

    print(Matrix.is_top_triangular_matrix(q))
    print(Matrix.is_top_triangular_matrix(x))

    print(Matrix.is_bottom_triangular_matrix(q))
    print(Matrix.is_bottom_triangular_matrix(x))

    print()
    wwq = s * q  # f+q , f*q, f-q, s*q, q*s
    for i in wwq.matrix:
        for j in i:
            print(j.value, end=" ")
        print()
    print()

    ww3 = s * f
    for i in ww3.matrix:
        for j in i:
            print(j.value, end=" ")
        print()
    print()

    ww4 = s * x
    for i in ww4.matrix:
        for j in i:
            print(j.value, end=" ")
        print()
    print()

    print((Integer(4) * Complex(5, 3)).value)
