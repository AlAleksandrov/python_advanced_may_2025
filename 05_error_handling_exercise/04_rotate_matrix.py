class MatrixSizeError(Exception):
    pass


class MatrixContentError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().split()

    if not line:
        break

    for x in line:
        if not x.isdigit():
            raise MatrixContentError("The matrix must consist of only integers")

    mtrx.append(line)


for row in mtrx:
    if len(row) != len(mtrx):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
