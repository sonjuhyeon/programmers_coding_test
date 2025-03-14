def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1  # f(0) = 0, f(1) = 1
    for _ in range(2, n + 1):
        a, b = b, a + b  # f(n-2) → f(n-1), f(n-1) → f(n)

    return b % 1234567
