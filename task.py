import math
import itertools


class Matrix:

    def __init__(self, *args):
        self.N = math.ceil(math.sqrt(len(args))) # square matrix dimension
        self.data = self.create_matrix(args)
        self.next_row = 0


    def create_matrix(self, *args):
        args = list(*args)
        data = [args[i * self.N : (i + 1) * self.N] for i in range(self.N)]
        
        for row in data:
            if len(row) < self.N:
                row.extend([0 for _ in range(self.N - len(row))])

        if len(data) < self.N:
            data.extend([[0 for _ in range(N)] for _ in range(self.N - len(data))])

        return data


    @classmethod
    def create_from_array(cls, array):
        flattened_array = tuple(itertools.chain.from_iterable(array))
        return Matrix(*flattened_array)


    def elementwise_operation(self, other, operation):
        if (other_is_matrix := isinstance(other, Matrix)) and self.N != other.N:
            raise TypeError('Matrices are of different dimensions')
        
        if not (other_is_matrix or isinstance(other, (int, float))):
            raise TypeError(f'Cannot perform operation on {type(Matrix)} and {type(other)}')

        result = [[None for _ in range(self.N)] for _ in range(self.N)]

        for i in range(self.N):
            for j in range(self.N):
                result[i][j] = operation(self.data[i][j], other.data[i][j] if other_is_matrix else other)

        return Matrix.create_from_array(result)
            

    def __add__(self, other):
        return self.elementwise_operation(other, lambda x, y : x + y)


    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        return self.elementwise_operation(other, lambda x, y : x - y)


    def __rsub__(self, other):
        return self.__sub__(other)


    def __mul__(self, other):
        return self.elementwise_operation(other, lambda x, y : x * y)


    def __rmult__(self, other):
        return self.__mul__(other)


    def __truediv__(self, other):
        return self.elementwise_operation(other, lambda x, y : x / y)


    def __matmul__(self, other):
        if (other_is_matrix := isinstance(other, Matrix)) and self.N != other.N:
            raise TypeError('Matrices are of different dimensions')
            
        result = [[0 for _ in range(self.N)] for _ in range(self.N)]

        for i in range(self.N):
            for j in range(self.N):
                for k in range(self.N):
                    result[i][j] += self.data[i][j] * other.data[i][j]

        return Matrix.create_from_array(result)


    def __iter__(self):
        return self


    def __next__(self):
        if self.next_row < self.N:
            self.next_row += 1
            return self.data[self.next_row - 1]
        else:
            self.next_row = 0
            raise StopIteration


    def __str__(self):        
        return '\n'.join(f'[{" ".join(str(round(n, 2)) for n in row)}]' for row in self.data)


if __name__ == '__main__':
    
    # If the number of arguments isn't enough to form a NxN matrix,
    # then the remaining cells are filled with 0. For example:
    #    1 2 3 4 5 results in [[1, 2, 3], [4, 5, 0], [0, 0, 0]]
    #    1 2 3 4   results in [[1, 2], [3, 4]]

    m1 = Matrix(1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9, 2)
    m2 = Matrix.create_from_array([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 5, 1], [5, 4, 2, 1]])

    print(f'm1:\n{m1}\n')
    print(f'm2:\n{m2}\n')

    m1_add_m2 = m1 + m2
    print(f'm1 + m2:\n{m1_add_m2}\n')

    m1_add_number = m1 + 5
    print(f'm1 + 5:\n{m1_add_number}\n')

    number_add_m1 = 5 + m1
    print(f'5 + m1:\n{number_add_m1}\n')

    m1_sub_m2 = m1 - m2
    print(f'm1 - m2:\n{m1_sub_m2}\n')

    m1_sub_number = m1 - 5
    print(f'm1 - 5:\n{m1_sub_number}\n')

    m1_mul_m2 = m1 * m2
    print(f'm1 * m2:\n{m1_mul_m2}\n')

    m1_div_m2 = m1 / m2
    print(f'm1 / m2:\n{m1_div_m2}\n')

    m1_matrix_mul_m2 = m1 @ m2
    print(f'm1 @ m2:\n{m1_matrix_mul_m2}\n')

    m2_matrix_mul_m1 = m2 @ m1
    print(f'm1 @ m2:\n{m2_matrix_mul_m1}\n')

    print('Using an iterator:')
    for row in m1:
        print(row)
