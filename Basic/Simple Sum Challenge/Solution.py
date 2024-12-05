def solveMeFirst(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    # Interactive input for testing
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Sum:", solveMeFirst(num1, num2))
