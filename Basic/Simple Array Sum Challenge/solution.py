def simpleArraySum(ar):
    """
    Calculates the sum of all integers in the array.

    Parameters:
        ar (list of int): A list of integers.

    Returns:
        int: The sum of the integers in the array.
    """
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input("Enter the number of elements in the array: ").strip())
    ar = list(map(int, input("Enter the array elements separated by space: ").rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()
