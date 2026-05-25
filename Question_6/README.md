# Calculate Eigenvalues of a Matrix

## Problem Statement
Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sort values from highest to lowest.

## Example
**Input:**
```python
matrix = [[2, 1], [1, 2]]
```
**Output:**
```python
[3.0, 1.0]
```
**Reasoning:**
The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, which for a 2x2 matrix is $\lambda^2 - \text{trace}(A)\lambda + \text{det}(A) = 0$, where $\lambda$ are the eigenvalues.

## Code Explanation
The logic is based on solving the characteristic equation for a 2x2 matrix: $\lambda^2 - \text{trace}(A)\lambda + \text{det}(A) = 0$.

1. For a $2 \times 2$ matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$:
   - The trace (sum of main diagonal elements) is $a + d$.
   - The determinant is $a \cdot d - b \cdot c$.
2. The roots of the characteristic equation are found using the quadratic formula:
   $$ \lambda = \frac{\text{trace} \pm \sqrt{\text{trace}^2 - 4 \cdot \text{determinant}}}{2} $$
3. The function calculates the `discriminant` ($\text{trace}^2 - 4 \cdot \text{determinant}$).
4. It then calculates the two eigenvalues (`lambda_1` and `lambda_2`) by adding and subtracting the square root of the discriminant. Since `discriminant**0.5` is added for `lambda_1`, it will naturally be the larger value, satisfying the requirement to sort from highest to lowest.
5. Finally, the function returns a list containing the two eigenvalues.
