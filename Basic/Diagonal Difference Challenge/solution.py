def diagonalDifference(arr):
    """
    Calculates the absolute difference between the sums of the two diagonals of a square matrix.

    Parameters:
        arr (list of list of int): A 2D list representing the square matrix.

    Returns:
        int: The absolute diagonal difference.
    """
    n = len(arr)
    primary_diagonal = sum(arr[i][i] for i in range(n))
    secondary_diagonal = sum(arr[i][n - i - 1] for i in range(n))
    return abs(primary_diagonal - secondary_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Enter the size of the square matrix: ").strip())

    arr = []
    print("Enter the rows of the matrix, one row per line:")
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
