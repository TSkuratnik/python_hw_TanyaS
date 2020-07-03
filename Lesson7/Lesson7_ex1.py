class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list
        self.m_len = len(matrix_list)
        self.m_str_len = len(matrix_list[0])

    def __str__(self):
        return (f'{self.matrix_list[i][n]}')

    def __add__(self, matrix2):
        self.matrix_list[i][n] = self.matrix_list[i][n] + matrix2[i][n]
        return self


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
m = Matrix(matrix1)
print(m.m_len)
print(m.m_str_len)

for i in range(m.m_len):
    for n in range(m.m_str_len):
        print(m, end=' ')
    print('\n')

for i in range(m.m_len):
    for n in range(m.m_str_len):
        m + matrix2
        print(m, end=' ')
    print('\n')
