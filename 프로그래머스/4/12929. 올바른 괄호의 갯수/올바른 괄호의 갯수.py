from math import comb
def solution(n):
    answer = comb(2 * n, n - 1) // n
    return answer