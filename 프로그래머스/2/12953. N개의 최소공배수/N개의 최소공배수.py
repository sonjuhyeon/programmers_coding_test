def greatest_common_divisor(n, m): #최대공약수
    if m == 0:
        return n
    else:
        return greatest_common_divisor(m, n % m)
    
def least_common_multiple(n, m): #최소공배수
    gcd = greatest_common_divisor(n, m)
    lcm = gcd * (n / gcd) * (m / gcd)
    return (lcm)
    
def solution(arr):
    for i in range(len(arr) - 1):
        lcm = least_common_multiple(arr[0], arr[i + 1])
        arr[0] = lcm
    answer = arr[0]
    return answer