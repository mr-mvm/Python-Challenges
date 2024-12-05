def plusMinus(arr):
    """
    Prints the proportions of positive, negative, and zero elements in the array.

    Parameters:
        arr (list of int): A list of integers.

    Returns:
        None: Prints the proportions to six decimal places.
    """
    n = len(arr)
    positive_count = sum(1 for x in arr if x > 0)
    negative_count = sum(1 for x in arr if x < 0)
    zero_count = sum(1 for x in arr if x == 0)

    print(f"{positive_count / n:.6f}")
    print(f"{negative_count / n:.6f}")
    print(f"{zero_count / n:.6f}")

if __name__ == '__main__':
    n = int(input("Enter the number of elements: ").strip())
    arr = list(map(int, input("Enter the elements separated by space: ").rstrip().split()))
    plusMinus(arr)
