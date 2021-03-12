from itertools import count


__memo = [2, 3, 5]


def nthPrime(n):
    for i in range(len(__memo), n):
        candidate = __memo[-1] + 2
        i = 0
        while True:
            p = __memo[i]
            i += 1
            if p * p > candidate:
                __memo.append(candidate)
                break
            elif candidate % p == 0:
                candidate += 2
                i = 0
                continue
    return __memo[n - 1]


def primes():
    yield from map(nthPrime, count(1))
