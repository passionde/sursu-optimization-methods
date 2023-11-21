def forward_elimination(matrix):
    matrix_len = len(matrix)
    for i in range(matrix_len):
        for k in range(i + 1, matrix_len):
            factor = matrix[k][i] / matrix[i][i]
            # print(f"factor = {factor} = [{k}, {i}] / [{i}, {i}]")
            for j in range(i, matrix_len + 1):
                # print(f"{matrix[k][j]}[{k}, {j}] -= {factor} * {matrix[i][j]}[{i}, {j}]")
                matrix[k][j] -= factor * matrix[i][j]
                # pprint.pprint(matrix)


def back_substitution(matrix):
    matrix_len = len(matrix)
    x = [0] * matrix_len
    for i in range(matrix_len - 1, -1, -1):
        x[i] = matrix[i][-1] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            matrix[k][-1] -= matrix[k][i] * x[i]
    return x


def gauss_elimination(matrix):
    try:
        forward_elimination(matrix)
        return back_substitution(matrix)
    except ZeroDivisionError:
        raise ValueError("There is no decision")


def print_solution(solution):
    print("Solution:")

    for num, x in enumerate(solution, start=1):
        print(f"\tX{num} = {x}")


if __name__ == "__main__":
    # Example usage:
    matrix = [
        [2, 2, 8],
        [1, 2, 20],
    ]

    try:
        print_solution(gauss_elimination(matrix))
    except ValueError:
        print("Нет решения")
