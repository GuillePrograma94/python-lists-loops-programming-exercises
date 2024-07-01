# Your code here


def matrix_builder(n):
    matrix = []
    for i in range(n):
        matrix.append([1] * n)
    return matrix

print(matrix_builder(3))