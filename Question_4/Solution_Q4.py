def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    m, n = len(matrix), len(matrix[0])

    if mode == "row":
        for i in range(m):
            summ = 0
            for j in range(n):
                summ += matrix[i][j]
            means.append(summ/n)

    if mode == "column":
        for i in range(n):
            summ = 0
            for j in range(m):
                summ += matrix[j][i]
            means.append(summ/m)

    return means
