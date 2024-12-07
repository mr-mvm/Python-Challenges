def solveMeFirst(a, b):
    """
    Returns the sum of two integers.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    res = solveMeFirst(num1, num2)
    print(res)
