from itertools import combinations

def solution(nums):
    answer = 0
    nums.sort()
    max_num = sum(nums[-3:])
    primes = [True] * (max_num + 1)
    primes[0], primes[1] = False, False
    
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i] == True:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
                
    comb = combinations(nums, 3)
    
    for c in comb:
        num = sum(c)
        if primes[num]:
            answer += 1
    
    return answer