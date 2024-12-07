def compareTriplets(a, b):
    """
    Compares two lists of integers element-wise and calculates scores for Alice and Bob.

    Parameters:
        a (list of int): The scores given to Alice.
        b (list of int): The scores given to Bob.

    Returns:
        list of int: A two-element list where the first element is Alice's score,
                     and the second is Bob's score.
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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input("Enter Alice's scores separated by space: ").rstrip().split()))
    b = list(map(int, input("Enter Bob's scores separated by space: ").rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
