class Matrix2x2:
    def __init__(self, x11, x12, x21, x22):
        self.data = [x11, x12, x21, x22]

    def dot_product(self, m2):
        pass

    def __add__(self, m2):
        if isinstance(m2, Matrix2x2):
            return Matrix2x2(*[self.data[i] + m2.data[i] for i in range(4)])
        elif isinstance(m2, int) or isinstance(m2, float):
            return Matrix2x2(*[self.data[i] + m2 for i in range(4)])
        else:
            print('Argument must be of type Matrix2x2')

    def __radd__(self, m2):
        return self.__add__(m2)

    def __str__(self):
        return f'{self.data[0]} {self.data[1]}\n{self.data[2]} {self.data[3]}'


if __name__ == '__main__':
    matrix_1 = Matrix2x2(4., 5., 6., 7.)
    matrix_2 = Matrix2x2(2., 2., 2., 1.)

    print(f'Matrix 1:\n{matrix_1}\n')
    print(f'Matrix 2:\n{matrix_2}\n')
    print(f'Sum of matrices:\n{matrix_1 + matrix_2}\n')
    print(f'Matrix 1 plus 5.3:\n{matrix_1 + 5.3}\n')
    print(f'5.3 + Matrix 1:\n{5.3 + matrix_1}\n')