# Question 1: Matrix-Vector Dot Product

**Difficulty:** Easy  
**Topic:** Linear Algebra  
**Link:** [https://www.deep-ml.com/problems/1](https://www.deep-ml.com/problems/1)

## Problem Description
Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

You may assume the input matrix is a valid (non-jagged) list of lists and the vector is a non-empty list.

### Example:
**Input:**
`a = [[1, 2], [2, 4]], b = [1, 2]`

**Output:**
`[5, 10]`

**Reasoning:**
Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; Row 2: (2 * 1) + (4 * 2) = 2 + 8 = 10

## Solution Explanation
The provided solution computes the dot product manually by iterating through each row of the matrix `a` and summing the element-wise products with the vector `b`.

### Logic:
1. **Dimension Check:** The code first verifies if the number of columns in matrix `a` (`len(a[0])`) matches the length of vector `b`. If they are unequal, it returns `-1` as the operation is mathematically invalid.
2. **Matrix Iteration:** It loops through each row of matrix `a` using the index `i`.
3. **Dot Product Calculation:** For each row, it loops through its elements and the corresponding elements in vector `b` (using index `j`), multiplying them and accumulating the result in the `indi` variable.
4. **Result Assembly:** After finishing a row, `indi` is appended to the `out` list, forming the resulting vector.

### Complexity:
- **Time Complexity:** $O(n \times m)$ where $n$ is the number of rows and $m$ is the number of columns in matrix `a`. We visit every element once.
- **Space Complexity:** $O(n)$ where $n$ is the number of rows, to store and return the resulting vector of size $n$.
