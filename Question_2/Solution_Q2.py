def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    if not a:
        return []
    m, n = len(a), len(a[0])

    b = []
    for _ in range(n):
        b.append([0] * m)

    for i in range(m):
        for j in range(n):
            b[j][i] = a[i][j]
    return b
