import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	T_m, T_n = len(T), len(T[0])
	A_m, A_n = len(A), len(A[0])
	S_m, S_n = len(S), len(S[0])

	# Checking if transformation for whole sequesce is even possible, and taking m instead of n for T because we need inverse of T for complete transformation
	if T_m != A_m or A_n != S_m:
		return -1

	# Checking for Invertible matrices of T and S
	if len(T[0]) != len(T) or len(S[0]) != len(S) or len(T) != len(S) or np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
		return -1

	T_inverse = np.linalg.inv(T)
	transformed_matrix = T_inverse @ A @ S
	return transformed_matrix.tolist()
