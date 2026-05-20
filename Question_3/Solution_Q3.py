import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    # Write your code here and return a python list after reshaping by using numpy's tolist() method
    m, n = len(a), len(a[0])
    nm, nn = new_shape

    reshaped_matrix = []
    for _ in range(nm):
        reshaped_matrix.append([0]*nn)

    if m*n != nm*nn:
        return []

    flatened = []
    for aa in a:
        for aaa in aa:
            flatened.append(aaa)

    count = 0
    for i in range(nm):
        for j in range(nn):
            reshaped_matrix[i][j] = flatened[count]
            count += 1
    
    return reshaped_matrix
