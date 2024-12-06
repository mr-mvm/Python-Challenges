def birthdayCakeCandles(candles):
    """
    Returns the count of the tallest candles that can be blown out.

    Parameters:
        candles (list of int): A list of integers representing the heights of candles.

    Returns:
        int: The number of tallest candles.
    """
    tallest = max(candles)
    return candles.count(tallest)

if __name__ == '__main__':
    candles_count = int(input("Enter the number of candles: ").strip())
    candles = list(map(int, input(f"Enter {candles_count} candle heights separated by space: ").rstrip().split()))
    print(birthdayCakeCandles(candles))
