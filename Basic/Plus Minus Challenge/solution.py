def plusMinus(arr):
    """
    Calculates and prints the ratios of positive, negative, and zero elements in an array.

    Parameters:
        arr (list of int): A list of integers.

    Returns:
        None: Prints the ratios rounded to 6 decimal places.
    """
    n = len(arr)
    positive = sum(1 for x in arr if x > 0)
    negative = sum(1 for x in arr if x < 0)
    zero = sum(1 for x in arr if x == 0)
    
    print(f"{positive / n:.6f}")
    print(f"{negative / n:.6f}")
    print(f"{zero / n:.6f}")

if __name__ == '__main__':
    n = int(input("Enter the number of elements: ").strip())
    arr = list(map(int, input("Enter the elements separated by space: ").rstrip().split()))
    plusMinus(arr)
