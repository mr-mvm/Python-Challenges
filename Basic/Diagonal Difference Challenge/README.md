# Diagonal Difference Challenge

## Overview
The **Diagonal Difference Challenge** is a Python exercise to calculate the absolute difference between the sums of the two diagonals of a square matrix.

## Problem Statement
Write a function `diagonalDifference(arr)` that:
1. Takes a square matrix `arr` as input.
2. Calculates:
    - The sum of the primary diagonal (top-left to bottom-right).
    - The sum of the secondary diagonal (top-right to bottom-left).
3. Returns the absolute difference between these two sums.

### Example
#### Input
`arr = [ [11, 2, 4], [4, 5, 6], [10, 8, -12] ]`

#### Output
`15`

#### Explanation
- Primary diagonal: `11 + 5 + (-12) = 4`
- Secondary diagonal: `4 + 5 + 10 = 19`
- Absolute difference: `|4 - 19| = 15`

## Files
- **solution.py**: Contains the implementation of the function.
- **testcase.py**: Includes unit tests to validate the function.

## How to Run
1. Save the `solution.py` and `testcase.py` files in the same directory.
2. Run `testcase.py` to execute the unit tests.
3. Alternatively, execute `solution.py` to test the function interactively.

## Edge Cases
1. The matrix is a single element.
2. The matrix contains all zeros.
3. The matrix contains only negative numbers.
4. The matrix is larger than 3x3 (e.g., 4x4 or 5x5).
