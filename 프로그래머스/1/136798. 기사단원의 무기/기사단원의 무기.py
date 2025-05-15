import math

def divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):  
        if n % i == 0:
            count += 1 if i == n // i else 2 
    return count

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        answer += divisors(i) if divisors(i) <= limit else power


    return answer