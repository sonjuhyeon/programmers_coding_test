def get_base_k(n, k):
    res = ""
    while n > 0:
        res = str(n % k) + res
        n = n // k
    return res
    
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
def solution(n, k):
    answer = 0
    base_k_of_n = get_base_k(n, k)
    numbers = base_k_of_n.split("0")
    
    for number in numbers:
        if number and is_prime(int(number)):
            answer += 1
    return answer