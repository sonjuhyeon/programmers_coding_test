def get_fibo(n, fibo):
    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
        

def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibo = [None] * (n + 1)
    fibo[0], fibo[1] = 0, 1
    get_fibo(n, fibo)
    return fibo[n] % 1234567