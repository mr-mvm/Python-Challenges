def birthdayCakeCandles(candles):
    """
    Determines the number of the tallest candles that can be blown out.

    Parameters:
        candles (list of int): Heights of the candles.

    Returns:
        int: The count of the tallest candles.
    """
    tallest = max(candles)
    return candles.count(tallest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input("Enter the number of candles: ").strip())
    candles = list(map(int, input("Enter the heights of the candles separated by space: ").rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
