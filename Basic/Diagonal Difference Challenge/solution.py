def diagonalDifference(arr):
    """
    Calculates the absolute difference between the sums of the two diagonals of a square matrix.

    Parameters:
        arr (list of list of int): A 2D square matrix.

    Returns:
        int: The absolute difference between the two diagonal sums.
    """
    primary_diagonal = sum(arr[i][i] for i in range(len(arr)))
    secondary_diagonal = sum(arr[i][len(arr) - 1 - i] for i in range(len(arr)))
    return abs(primary_diagonal - secondary_diagonal)

if __name__ == '__main__':
    # Input handling for the interactive program
    n = int(input("Enter the size of the square matrix (n x n): ").strip())
    arr = []
    print("Enter the rows of the matrix:")
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print("Diagonal Difference:", result)
