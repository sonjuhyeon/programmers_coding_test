def matrix_mult(A, B, mod=1234567):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]

def matrix_power(mat, n, mod=1234567):
    res = [[1, 0], [0, 1]]  # 단위 행렬
    base = mat
    
    while n:
        if n % 2:  # 홀수이면 곱해줌
            res = matrix_mult(res, base, mod)
        base = matrix_mult(base, base, mod)  # 제곱
        n //= 2
    
    return res

def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    F = [[1, 1], [1, 0]]  # 기본 행렬
    result = matrix_power(F, n - 1)
    
    return result[0][0]  # F(n)