def solution(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i] == True:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return sum(primes)