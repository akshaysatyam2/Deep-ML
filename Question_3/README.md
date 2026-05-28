# Question 3: Reshape Matrix

**Difficulty:** Easy  
**Topic:** Linear Algebra  
**Link:** [https://www.deep-ml.com/problems/3](https://www.deep-ml.com/problems/3)

## Problem Statement
Write a Python function that reshapes a given matrix into a specified shape. If it can't be reshaped, return an empty list `[]`.

## Example
**Input:**
`a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)`

**Output:**
`[[1, 2], [3, 4], [5, 6], [7, 8]]`

**Reasoning:**
The given matrix is reshaped from 2x4 to 4x2.

## Code Explanation
The provided solution performs the reshaping operation manually by flattening the original matrix and then filling a new matrix of the target shape.

### Logic:
1. **Dimension Retrieval:** It calculates the dimensions of the original matrix `(m, n)` and extracts the target dimensions `(nm, nn)` from `new_shape`.
2. **Pre-allocation:** A new matrix named `reshaped_matrix` of dimensions `nm x nn` is created and initialized with zeros.
3. **Validity Check:** It checks if the total number of elements in the original matrix (`m * n`) matches the total number of elements required for the new shape (`nm * nn`). If not, it's impossible to reshape, and it returns an empty list `[]`.
4. **Flattening:** It iterates through every row and element of the original matrix `a` and appends them to a 1D list called `flatened`.
5. **Reconstruction:** It uses a nested loop to iterate through the indices of the `reshaped_matrix`. Using a `count` variable to keep track of the current index in the `flatened` list, it populates the new matrix row by row.

### Complexity:
- **Time Complexity:** $O(m \times n)$ where $m$ is the number of rows and $n$ is the number of columns in the original matrix. The algorithm iterates over all elements to flatten them and then again to reconstruct the matrix.
- **Space Complexity:** $O(m \times n)$ to store the `flatened` 1D array and the resulting `reshaped_matrix`.