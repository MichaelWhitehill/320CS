# A program to compute a logically recursive formula, using both
# recursion (divide and conquer) and building up a table of answers
# to subproblems (dynamic programming).
# Which do you think will be faster, for which sizes of input?
# Do you think dynamic programming can be used to make MergeSort
# (another divide and conquer algorithm) faster?

import sys

coins = []
calls = 0
reads = 0
sortCoins = []


# read coin values
def readCoins(fnm):
    global coins
    f = open(fnm)
    for line in f:
        l = line.strip().split(" ")
        for c in l:
            coins.append(int(c))
    if db: print("coins:", coins)


def mkChangeDC(n, c):
    """Divide and Conquer. n is the amount to make change for.
    Should only consider coins with indices [0, c] (inclusive inclusive)."""
    global calls
    global sortCoins
    if not sortCoins:
        sortCoins = sorted(coins)
    count = 0
    calls = calls + 1
    if n == 0:
        return 1
    if n < 0:
        return 0
    if c < 0:
        return 0

    if sortCoins[c] == 1:
        count = count +1

    else:
        for i in range(0, n // sortCoins[c] +1):
            count = count + mkChangeDC(n - i * sortCoins[c], c - 1)

    return count


def mkChangeDP(n):
    """Dynamic Programming. n is the amount to make change for.
    Should consider all coins."""
    global reads
    # dynTable = [[x for x in range(len(coins))] for x in range(n+1)]

    ways = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            ways[i] += ways[i - coin]
            reads += 1

    return ways[n]


if __name__ == "__main__":
    db = len(sys.argv) > 3
    n = int(sys.argv[1])
    fnm = sys.argv[2]
    readCoins(fnm)
    c = len(coins) - 1
    ways = mkChangeDC(n, c)
    print("mkChangeDC")
    print("amount:", n, "coins:", coins, "ways:", ways, "calls:", calls)
    ways = mkChangeDP(n + 1)
    print("mkChangeDP")
    print("amount:", n, "coins:", coins, "ways:", ways, "reads:", reads)
