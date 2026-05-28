import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    T_m, T_n = len(T), len(T[0])
    A_m, A_n = len(A), len(A[0])
    S_m, S_n = len(S), len(S[0])

    # Checking if transformation for the sequence is even possible
    if T_m != A_m or A_n != S_m:
        return -1

    # Checking for Invertible matrices of T and S
    # Matrices must be square to have an inverse
    if T_m != T_n or S_m != S_n or np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
        return -1

    T_inverse = np.linalg.inv(T)
    transformed_matrix = T_inverse @ A @ S
    return transformed_matrix.tolist()
