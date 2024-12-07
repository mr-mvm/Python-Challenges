# Time Conversion Challenge

## Overview
The **Time Conversion Challenge** is a Python exercise to convert a 12-hour AM/PM formatted time string into a 24-hour military time format.

## Problem Statement
Write a function `timeConversion(s)` that:
1. Accepts a string `s` representing the time in 12-hour AM/PM format (e.g., "07:05:45PM").
2. Converts it into a string representing the time in 24-hour format (e.g., "19:05:45").
3. Returns the converted time as a string.

## Example
### Input
`12:00:00AM`
### Output
`00:00:00`

### Input
`12:00:00PM`
### Output
`12:00:00`

### Input
`07:05:45PM`
### Output
`19:05:45`

## Files
- **solution.py**: Contains the implementation of the function.
- **testcase.py**: Includes unit tests to validate the function.

## How to Run
1. Save the `solution.py` and `testcase.py` files in the same directory.
2. Run `testcase.py` to execute the unit tests.
3. Alternatively, execute `solution.py` to test the function interactively.
