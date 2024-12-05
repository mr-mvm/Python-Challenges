def compareTriplets(a, b):
    """
    Compares two lists of integers and awards points for each comparison.

    Parameters:
        a (list of int): List of integers representing Alice's scores.
        b (list of int): List of integers representing Bob's scores.

    Returns:
        list of int: A list containing two integers, the scores for Alice and Bob respectively.
    """
    alice_score = 0
    bob_score = 0

    for alice, bob in zip(a, b):
        if alice > bob:
            alice_score += 1
        elif bob > alice:
            bob_score += 1

    return [alice_score, bob_score]

if __name__ == '__main__':
    # Input handling for the interactive program
    a = list(map(int, input("Enter Alice's scores separated by space: ").rstrip().split()))
    b = list(map(int, input("Enter Bob's scores separated by space: ").rstrip().split()))
    result = compareTriplets(a, b)
    print("Scores: Alice =", result[0], ", Bob =", result[1])
