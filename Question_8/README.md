# Calculate 2x2 Matrix Inverse

**Difficulty:** Easy
**Topic:** Linear Algebra
**Link:** [Deep-ML Problem 8](https://www.deep-ml.com/problems/8)

## Problem Statement

Write a Python function that calculates the inverse of a 2x2 matrix. The inverse of a matrix A is another matrix A_inv such that A * A_inv = I (the identity matrix).

For a 2x2 matrix `[[a, b], [c, d]]`, the inverse exists only if the determinant `(ad - bc)` is non-zero.

Return `None` if the matrix is not invertible (i.e., when the determinant equals zero).

## Example

**Input:**
```python
matrix = [[4, 7], [2, 6]]
```

**Output:**
```python
[[0.6, -0.7], [-0.2, 0.4]]
```

**Reasoning:**
For matrix `[[a, b], [c, d]] = [[4, 7], [2, 6]]`:
Calculate determinant: `det = ad - bc = 4×6 - 7×2 = 24 - 14 = 10`
Since `det ≠ 0`, the matrix is invertible
Apply formula: `A⁻¹ = (1/det) × [[d, -b], [-c, a]] = (1/10) × [[6, -7], [-2, 4]] = [[0.6, -0.7], [-0.2, 0.4]]`

## Code Explanation

The solution first checks the dimensions of the input matrix to ensure it's a 2x2 matrix. It then extracts the individual elements `a`, `b`, `c`, and `d` from the matrix. The determinant is calculated using the formula `det = a * d - b * c`. 

If the determinant is zero, the matrix is singular (not invertible), and the function returns `None`. If the determinant is non-zero, it proceeds to calculate the inverse matrix using the formula for a 2x2 matrix: scaling the matrix `[[d, -b], [-c, a]]` by `1 / det`. The result is a new 2x2 list with the calculated values.
