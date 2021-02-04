class MyEr(Exception):

    def __init__(self, msg):
        self.msg = msg


class Matrix:

    def __init__(self, matrix, rows_and_col, const_multiply=None):
        self.matrix = matrix
        self.rows_and_col = rows_and_col
        self.const_multiply = const_multiply
        self.output_sum = []
        self.output_mul_const = []
        self.output_mul_matrix = []
        self.out = ''
        self.action = None
        self.transposition_matrix = []

    def __str__(self):
        for lines in self.matrix:
            str_temp = ''
            for el in range(0, len(lines)):
                str_temp += f'{str(lines[el])} '
            self.out += str_temp + '\n'
        return f'The result is:\n{self.out}'

    def __add__(self, other):
        if self.rows_and_col != other.rows_and_col:
            return MyEr('The operation cannot be performed.\n')
        else:
            for line in range(0, len(self.matrix)):
                temp_stor_for_add = []
                for el in range(0, len(self.matrix[line])):
                    temp_el_for_add = float(self.matrix[line][el]) + float(other.matrix[line][el])
                    temp_stor_for_add.append(temp_el_for_add)
                self.output_sum.append(temp_stor_for_add)
            return Matrix(self.output_sum, rows_and_col=None)

    def __mul__(self, other):
        if other.const_multiply is not None:
            for line in range(0, len(self.matrix)):
                storage_temp_for_mul = []
                for el in range(0, len(self.matrix[line])):
                    temp_el_for_mul = float(self.matrix[line][el]) * float(other.const_multiply)
                    storage_temp_for_mul.append(temp_el_for_mul)
                self.output_mul_const.append(storage_temp_for_mul)
            return Matrix(self.output_mul_const, rows_and_col=None)
        else:
            if self.rows_and_col[1] == other.rows_and_col[0]:
                for lines in range(0, len(self.matrix)):
                    column = 0
                    line_for_new_matrix = []
                    while column != len(other.matrix[0]):
                        list_of_elem_of_new_line = []
                        for el in range(0, len(self.matrix[lines])):
                            mul_of_elem = float(self.matrix[lines][el]) * float(other.matrix[el][column])
                            list_of_elem_of_new_line.append(mul_of_elem)
                        line_for_new_matrix.append(sum(list_of_elem_of_new_line))
                        column += 1
                    self.output_mul_matrix.append(line_for_new_matrix)
            else:
                return MyEr('The operation cannot be performed.\n')
            return Matrix(self.output_mul_matrix, rows_and_col=None)

    def transpose_matrix(self, method_of_transpose):
        if method_of_transpose < 3:
            # self.transposition_matrix = []
            column = 0
            while column != len(self.matrix[0]):
                lines_temporary = []

                for lines in range(0, len(self.matrix)):
                    lines_temporary.append(self.matrix[lines][column])

                if method_of_transpose == 2:
                    lines_temporary.reverse()

                self.transposition_matrix.append(lines_temporary)
                column += 1

            if method_of_transpose == 2:
                self.transposition_matrix.reverse()

            return Matrix(self.transposition_matrix, rows_and_col=None)

        else:
            for lines in self.matrix:
                if method_of_transpose == 3:
                    lines.reverse()
                self.transposition_matrix.append(lines)
            if method_of_transpose == 4:
                self.transposition_matrix.reverse()

            return Matrix(self.transposition_matrix, rows_and_col=None)

    @classmethod
    def find_determinant(cls, matrix):
        if len(matrix) == 1:
            return matrix[0][0]

        elif len(matrix) == 2 and len(matrix[0]) == 2:
            deter = float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
            return deter

        else:
            determinant = []
            for el_for_multiply in range(len(matrix[0])):
                # print(matrix[0][el_for_multiply])
                two_two_matrix = []

                for lines in range(len(matrix)):
                    rows_matrix = []
                    for el in range(len(matrix[lines])):
                        if lines != 0 and el != el_for_multiply:
                            rows_matrix.append(float(matrix[lines][el]))

                    if rows_matrix:
                        two_two_matrix.append(rows_matrix)
                det = float(matrix[0][el_for_multiply]) * (-1) ** (0 + el_for_multiply) * cls.find_determinant(
                    two_two_matrix)
                if det:
                    determinant.append(det)

        return sum(determinant)

    @classmethod
    def do_cofactors_matrix(cls, matrix):
        if len(matrix) == 1:
            return matrix[0][0]

        elif len(matrix) == 2 and len(matrix[0]) == 2:
            det = float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
            return det

        else:
            cofactors_matrix = []

            for row in range(len(matrix)):
                cofactors_rows = []
                for el_for_multiply in range(len(matrix[row])):
                    two_two_matrix = []

                    for lines in range(len(matrix)):
                        rows_matrix = []

                        for el in range(len(matrix[lines])):
                            if lines != row and el != el_for_multiply:
                                rows_matrix.append(float(matrix[lines][el]))
                        if rows_matrix:
                            two_two_matrix.append(rows_matrix)

                    cofactor = (-1) ** (row + el_for_multiply) * cls.find_determinant(two_two_matrix)
                    cofactors_rows.append(cofactor)

                cofactors_matrix.append(cofactors_rows)

        return cofactors_matrix

    @staticmethod
    def do_matrix(rows):
        count = 0
        list_of_matrices = []
        while count < rows:
            row_mat = input().split()
            list_of_matrices.append(row_mat)
            count += 1
        return list_of_matrices

    @staticmethod
    def build_a_matrix(size_of_matrix):
        matrix = Matrix.do_matrix(int(size_of_matrix[0]))
        matrix = Matrix(matrix, size_of_matrix)
        return matrix


class Menu:

    def __init__(self):
        self.multiply_to_const = None
        self.sum_of_matrices = None
        self.multiply_to_matrix = None
        self.transpose_matrix = None
        self.determinant = 0
        self.inversion_matrix = None

    def what_to_do(self):
        action = ''
        while action != '0':
            action = input(
                '1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n'
                '6. Inverse matrix\n0. Exit\nYour choice: ')
            if action == '1':
                size_of_first_matrix = input('Enter size of first matrix: ').split()
                print('Enter first matrix: ')
                first_matrix = Matrix.build_a_matrix(size_of_first_matrix[0])

                size_of_second_matrix = input('Enter size of second matrix: ').split()
                print('Enter second matrix: ')
                second_matrix = Matrix.build_a_matrix(size_of_second_matrix[0])

                self.sum_of_matrices = first_matrix + second_matrix
                print(self.sum_of_matrices)
            elif action == '2':
                size_of_matrix = input('Enter size of first matrix: ').split()
                print('Enter matrix: ')
                matrix = Matrix.build_a_matrix(size_of_matrix[0])

                const = int(input('Enter constant: '))
                const = Matrix(matrix=None, rows_and_col=None, const_multiply=const)
                self.multiply_to_const = matrix * const
                print(self.multiply_to_const)
            elif action == '3':
                size_of_first_matrix = input('Enter size of first matrix: ').split()
                print('Enter first matrix: ')
                first_matrix_for_mul = Matrix.build_a_matrix(size_of_first_matrix)

                size_of_second_matrix = input('Enter size of second matrix: ').split()
                print('Enter second matrix: ')
                second_matrix_for_mul = Matrix.build_a_matrix(size_of_second_matrix)

                self.multiply_to_matrix = first_matrix_for_mul * second_matrix_for_mul
                print(self.multiply_to_matrix)
            elif action == '4':
                doing = int(
                    input('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice: '))
                size_of_matrix = input('Enter matrix size: ').split()
                print('Enter matrix: ')
                matrix = Matrix.build_a_matrix(size_of_matrix)

                self.transpose_matrix = matrix.transpose_matrix(doing)
                print(self.transpose_matrix)
            elif action == '5':
                size_of_matrix = input('Enter matrix size: ').split()
                if size_of_matrix[0] == size_of_matrix[1]:
                    print('Enter matrix: ')
                    matrix = Matrix.do_matrix(int(size_of_matrix[0]))

                    self.determinant = Matrix.find_determinant(matrix)
                    print(self.determinant)
                else:
                    return MyEr('The operation cannot be performed.\n')
            elif action == '6':
                size_of_matrix = input('Enter matrix size: ').split()
                if size_of_matrix[0] == size_of_matrix[1]:
                    print('Enter matrix: ')
                    matrix = Matrix.do_matrix(int(size_of_matrix[0]))
                    det_matrix = Matrix.find_determinant(matrix)
                    if det_matrix != 0:
                        det_matrix = Matrix(matrix=None, rows_and_col=None, const_multiply=(1/det_matrix))

                        cofactors_matrix = Matrix.do_cofactors_matrix(matrix)
                        cofactors_matrix = Matrix(cofactors_matrix, size_of_matrix)
                        cofactors_matrix = cofactors_matrix.transpose_matrix(1)

                        self.inversion_matrix = cofactors_matrix * det_matrix
                        print(self.inversion_matrix)
                    else:
                        return MyEr('The operation cannot be performed. Division by zero\n')
                else:
                    return MyEr('The operation cannot be performed.\n')


result = Menu()
print(result.what_to_do())
