# Compare the Triplets Challenge

## Overview
The **Compare the Triplets Challenge** is a Python exercise to compare two lists of integers and calculate scores for two participants, Alice and Bob.

## Problem Statement
Write a function `compareTriplets(a, b)` that:
1. Takes two lists of integers `a` and `b`, representing the scores of Alice and Bob across three criteria.
2. Compares the scores element by element:
    - If Alice's score is greater, she gets 1 point.
    - If Bob's score is greater, he gets 1 point.
    - If the scores are equal, no points are awarded.
3. Returns a list of two integers: `[Alice's score, Bob's score]`.

### Example
#### Input
`a = [5, 6, 7]`  
`b = [3, 6, 10]`

#### Output
`[1, 1]`

#### Explanation
- Alice gets 1 point for the first criterion (5 > 3).
- Bob gets 1 point for the third criterion (10 > 7).
- No points for the second criterion (6 = 6).

## Files
- **solution.py**: Contains the implementation of the function.
- **testcase.py**: Includes unit tests to validate the function.

## How to Run
1. Save the `solution.py` and `testcase.py` files in the same directory.
2. Run `testcase.py` to execute the unit tests.
3. Alternatively, execute `solution.py` to test the function interactively.
