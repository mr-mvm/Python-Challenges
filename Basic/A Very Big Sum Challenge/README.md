# A Very Big Sum Challenge

## Overview
The **A Very Big Sum Challenge** is a Python exercise to compute the sum of a list of integers, including potentially very large numbers.

## Problem Statement
Write a function `aVeryBigSum(ar)` that:
1. Takes a list of integers `ar`.
2. Returns the sum of the integers in the list.

### Example
#### Input
`ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]`

#### Output
`5000000015`

#### Explanation
The sum of the integers in the array is `1000000001 + 1000000002 + 1000000003 + 1000000004 + 1000000005 = 5000000015`.

## Files
- **solution.py**: Contains the implementation of the function.
- **testcase.py**: Includes unit tests to validate the function.

## How to Run
1. Save the `solution.py` and `testcase.py` files in the same directory.
2. Run `testcase.py` to execute the unit tests.
3. Alternatively, execute `solution.py` to test the function interactively.

## Edge Cases
1. The list contains only one element.
2. The list contains all zeros.
3. The list contains negative numbers.
4. The list contains a mix of positive and negative numbers.
5. The list contains extremely large integers.
