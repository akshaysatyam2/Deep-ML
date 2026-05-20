# Question 4: Calculate Mean by Row or Column

**Difficulty:** Easy  
**Topic:** Linear Algebra  
**Link:** [https://www.deep-ml.com/problems/4](https://www.deep-ml.com/problems/4)

## Problem Description
Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.

### Example:
**Input:**
`matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'`

**Output:**
`[4.0, 5.0, 6.0]`

**Reasoning:**
Calculating the mean of each column results in `[(1+4+7)/3, (2+5+8)/3, (3+6+9)/3]`.

## Solution Explanation
The provided solution iterates over the matrix based on the specified `mode` to calculate the mean.

### Logic:
1. **Dimension Extraction:** The function retrieves the number of rows `m` and the number of columns `n`.
2. **Row Mode:** If the mode is "row", the outer loop iterates through each row. The inner loop sums all elements in that row. It then divides the sum by `m` to find the average, appending it to the `means` list.
3. **Column Mode:** If the mode is "column", the outer loop iterates through each column index. The inner loop traverses down the rows for that specific column, summing the elements. It then divides the sum by `n` and appends it to `means`.

*(Note: There is a logic flaw in this calculation for non-square matrices. For row means, the sum should be divided by the number of elements in the row, which is `n`. For column means, the sum should be divided by the number of elements in the column, which is `m`.)*

### Complexity:
- **Time Complexity:** $O(m \times n)$ where $m$ is the number of rows and $n$ is the number of columns, because every element is visited once.
- **Space Complexity:** $O(m)$ or $O(n)$ depending on the mode, to store the resulting means list.