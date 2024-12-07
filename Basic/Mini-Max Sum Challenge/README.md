# Mini-Max Sum Challenge

## Overview
The **Mini-Max Sum Challenge** is a Python exercise to calculate and display the minimum and maximum sums of an array by excluding one element at a time.

## Problem Statement
Write a function `miniMaxSum(arr)` that:
1. Accepts an array `arr` of integers.
2. Calculates:
    - The minimum sum by excluding the largest element.
    - The maximum sum by excluding the smallest element.
3. Prints the minimum and maximum sums separated by a space.

### Example
For the input `arr = [1, 2, 3, 4, 5]`:

Output:
'10' '14'
Explanation:
• Minimum sum: 1 + 2 + 3 + 4 = 10 (excluding 5).
• Maximum sum: 2 + 3 + 4 + 5 = 14 (excluding 1).

## Files
- **solution.py**: Contains the implementation of the function.
- **testcase.py**: Includes unit tests to validate the function.

## How to Run
1. Save the `solution.py` and `testcase.py` files in the same directory.
2. Run `testcase.py` to execute the unit tests.
3. Alternatively, execute `solution.py` to test the function interactively.
