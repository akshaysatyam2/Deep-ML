# Matrix Transformation

## Problem Statement
Write a Python function that transforms a matrix `A` using transformation matrices `T` and `S`. The transformation formula is $T^{-1} A S$. 

The function must:
1. Check if the transformation is mathematically possible given the matrix dimensions.
2. Ensure both matrices `T` and `S` are invertible (they must be square and have non-zero determinants).
3. Return the transformed matrix as a Python list of lists, or return `-1` if the transformation is not possible or if either `T` or `S` is not invertible.

## Example
**Input:**
```python
A = [[1, 2], [3, 4]]
T = [[2, 0], [0, 2]]
S = [[1, 1], [0, 1]]
```
**Output:**
```python
[[0.5, 1.5], [1.5, 3.5]]
```

## Code Explanation
The transformation follows the formula: $T^{-1} A S$.
1. Extract the dimensions of all three matrices `A`, `T`, and `S`.
2. **Check if transformation for the whole sequence is possible:** The columns of $T^{-1}$ (which equals the rows of $T$, or `m`) must match the rows of $A$. This is why we check `T_m != A_m`. Additionally, the columns of $A$ (`A_n`) must match the rows of $S$ (`S_m`).
3. **Check for Invertible matrices of T and S:** A matrix is invertible if it is a square matrix (checked via `len(T[0]) != len(T)` and `len(S[0]) != len(S)`), has a non-zero determinant, and in this specific logic we also enforce that `T` and `S` are of the same dimensions (`len(T) != len(S)`). If any of these fail or their determinants are zero, it returns `-1`.
4. If valid, the inverse of `T` is computed using `numpy.linalg.inv(T)`.
5. The result of the multiplication $T^{-1} A S$ is calculated using the `@` operator.
6. Finally, the transformed numpy array is converted back to a list of lists using `.tolist()` and returned.
