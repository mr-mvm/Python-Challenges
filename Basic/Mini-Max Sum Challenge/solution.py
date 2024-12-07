def miniMaxSum(arr):
    """
    Calculates and prints the minimum and maximum sums of an array by summing all elements except one.

    Parameters:
        arr (list of int): A list of integers.

    Returns:
        None: Prints the minimum and maximum sums separated by a space.
    """
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input("Enter integers separated by space: ").rstrip().split()))
    miniMaxSum(arr)
