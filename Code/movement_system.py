def generate_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    center = size // 2

    for i in range(size):
        for j in range(size):
            matrix[i][j] = abs(center - i) + abs(center - j)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


size = 7
result_matrix = generate_matrix(size)

print_matrix(result_matrix)
