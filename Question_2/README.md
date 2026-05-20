# Question 2: Transpose of a Matrix

**Difficulty:** Easy  
**Topic:** Linear Algebra  
**Link:** [https://www.deep-ml.com/problems/2](https://www.deep-ml.com/problems/2)

## Problem Description
Write a Python function that computes the transpose of a given 2D matrix. The transpose of a matrix is formed by turning its rows into columns and columns into rows. For an $m \times n$ matrix, the transpose will be an $n \times m$ matrix.

### Example:
**Input:**
`a = [[1, 2, 3], [4, 5, 6]]`

**Output:**
`[[1, 4], [2, 5], [3, 6]]`

**Reasoning:**
The input is a 2x3 matrix. The transpose swaps rows and columns: the first row `[1, 2, 3]` becomes the first column, and the second row `[4, 5, 6]` becomes the second column, resulting in a 3x2 matrix.

## Solution Explanation
The provided solution handles the transposition manually by creating a new matrix and copying the elements over with swapped indices.

### Logic:
1. **Edge Case Handling:** First, it checks if the input matrix `a` is empty. If it is, the function returns an empty list immediately.
2. **Dimension Retrieval:** It finds the dimensions of the original matrix: `m` (number of rows) and `n` (number of columns).
3. **Pre-allocation:** It initializes a new matrix `b` of dimensions $n \times m$, filling it with zeros to serve as a placeholder.
4. **Element Mapping:** It uses a nested loop to iterate through every element in the original matrix `a` at row `i` and column `j`. It assigns each element to its new swapped position in matrix `b` at row `j` and column `i`.

### Complexity:
- **Time Complexity:** $O(m \times n)$ where $m$ is the number of rows and $n$ is the number of columns in matrix `a`. We visit every element exactly once.
- **Space Complexity:** $O(m \times n)$ to create and store the new transposed matrix `b`.