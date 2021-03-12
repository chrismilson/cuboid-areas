from math import sqrt, ceil
from argparse import ArgumentParser
from itertools import count, combinations_with_replacement as combinations
from functools import reduce
from primes import primes


def totalAndSquare(k):
    """
    Calculates the total number of different areas and the number of those areas
    that are square for a number n = p^k for some prime p and positive integer
    k.
    """
    m = k >> 1
    return (
        m ** 2 + (2 + (k & 1)) * m + (1 + (k & 1)),
        m + 1
    )


def primePowerCounts(n):
    """
    When given a number n with prime factorisation p1^k1·p2^k2·...·pm^km,
    iterates over the numbers k1, k2, ..., km.
    """
    p = 2
    it = primes()
    while (p := next(it)) ** 2 <= n:
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        if count > 0:
            yield count
    if n > 1:
        yield 1


def reducer(acc, value):
    prevTotal, prevSquare = acc
    total, square = value

    return (
        prevTotal * total + (prevTotal - prevSquare) * (total - square),
        prevSquare * square
    )


def a140773(n):
    """
    Calculates the nth term of A140773 in the OEIS. Also the number of distinct
    areas when arranging n unit cubes into a cuboid.
    """
    return 1 if n == 1 else reduce(
        reducer,
        map(
            totalAndSquare,
            primePowerCounts(n)
        )
    )[0]


if __name__ == "__main__":
    parser = ArgumentParser(
        "Calculates the number of different areas obtained when arranging n "
        "identical cubes into a cuboid."
    )
    parser.add_argument(
        "integers", metavar="N", type=int,
        nargs="*", help="The integers to calculate the value for"
    )
    parser.add_argument(
        "-b", type=int,
        help="If present, will produce a b-file for the OEIS. The argument is "
        "the number of terms to calculate."
    )

    args = parser.parse_args()

    if args.b != None:
        # We will produce the b file
        with open("./b140773.txt", "w+") as file:
            for i in range(1, args.b + 1):
                file.write(f"{i} {a140773(i)}\n")
    else:
        for n in args.integers:
            print(f"{n}\t->\t{a140773(n)}")
