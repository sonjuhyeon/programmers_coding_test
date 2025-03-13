from itertools import permutations
from math import sqrt

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    
    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i] == True:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    return [i for i in range(n + 1) if is_prime[i]]

def solution(numbers):
    answer = 0
    perm_lst = set()
    for i in range(1, len(numbers) + 1):
        for perm in permutations(list(numbers), i):
            perm_lst.add(int("".join(perm)))
    
    primes = sieve(max(perm_lst))
    
    for n in perm_lst:
        if n in primes:
            answer += 1
            
    return answer