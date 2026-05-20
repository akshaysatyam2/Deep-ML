# Question 5: Scalar Multiplication of a Matrix

**Difficulty:** Easy  
**Topic:** Linear Algebra  
**Link:** [https://www.deep-ml.com/problems/5](https://www.deep-ml.com/problems/5)

## Problem Description
Write a Python function that multiplies a matrix by a scalar and returns the result.

### Example:
**Input:**
`matrix = [[1, 2], [3, 4]], scalar = 2`

**Output:**
`[[2, 4], [6, 8]]`

**Reasoning:**
Each element of the matrix is multiplied by the scalar.

## Solution Explanation
The provided solution modifies the given matrix in-place by iterating through each element and multiplying it by the provided scalar.

### Logic:
1. **Dimension Extraction:** Retrieve the number of rows `m` and columns `n` of the matrix.
2. **Iteration:** Use a nested loop to traverse every element at row `i` and column `j`.
3. **Multiplication:** Multiply the current element `matrix[i][j]` by the `scalar` and update the value directly in the original matrix.
4. **Return:** Return the modified matrix.

### Complexity:
- **Time Complexity:** $O(m \times n)$ where $m$ is the number of rows and $n$ is the number of columns, since every element is visited and multiplied once.
- **Space Complexity:** $O(1)$ auxiliary space. The matrix is modified in-place, meaning no additional large data structures are created to store the result.