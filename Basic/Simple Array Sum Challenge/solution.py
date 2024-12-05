def simpleArraySum(ar):
    """
    Returns the sum of all elements in the array.

    Parameters:
        ar (list of int): List of integers.

    Returns:
        int: Sum of all integers in the array.
    """
    return sum(ar)

if __name__ == '__main__':
    # Handling interactive input
    ar_count = int(input("Enter the number of elements: ").strip())
    ar = list(map(int, input("Enter the elements separated by space: ").rstrip().split()))
    result = simpleArraySum(ar)
    print("Sum of array elements:", result)
