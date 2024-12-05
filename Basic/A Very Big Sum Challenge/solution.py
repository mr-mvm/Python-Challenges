def aVeryBigSum(ar):
    """
    Calculates the sum of all elements in a list of integers.

    Parameters:
        ar (list of int): A list of integers.

    Returns:
        int: The sum of all integers in the list.
    """
    return sum(ar)

if __name__ == '__main__':
    # Input handling for the interactive program
    ar_count = int(input("Enter the number of elements: ").strip())
    ar = list(map(int, input("Enter the elements separated by space: ").rstrip().split()))
    result = aVeryBigSum(ar)
    print("Sum of array elements:", result)
