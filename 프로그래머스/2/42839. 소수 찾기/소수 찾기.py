from itertools import permutations
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):  # 2부터 √n까지만 확인
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    perm_lst = set()
    for i in range(1, len(numbers) + 1):
        for perm in permutations(list(numbers), i):
            perm_lst.add(int("".join(perm)))
    
    for n in perm_lst:
        if is_prime(n):
            answer += 1
            
    return answer