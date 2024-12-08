def staircase(n):
    """
    Prints a staircase of size n, where each level consists of spaces and hash symbols (#).

    Parameters:
        n (int): The height of the staircase.

    Returns:
        None: Prints the staircase.
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

if __name__ == '__main__':
    n = int(input("Enter the size of the staircase: ").strip())
    staircase(n)
