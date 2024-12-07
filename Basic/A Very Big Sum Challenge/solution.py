def aVeryBigSum(ar):
    """
    Calculates the sum of a list of integers.

    Parameters:
        ar (list of int): A list of integers.

    Returns:
        int: The sum of the integers in the list.
    """
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input("Enter the number of elements: ").strip())
    ar = list(map(int, input("Enter the elements separated by space: ").rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()
