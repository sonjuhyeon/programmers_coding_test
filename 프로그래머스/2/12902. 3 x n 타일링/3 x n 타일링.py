'''
n=2일 때는 3가지 방법이 있음.
n=4일 때는 dp[2] * 3 + 2 = 3 × 3 + 2 = 11
n=6일 때는 dp[4] * 3 + dp[2] * 2 + 2 = 11 × 3 + 3 × 2 + 2 = 41
'''

def solution(n):
    if n % 2 == 1:
        return 0  # 홀수는 만들 수 없음

    MOD = 1_000_000_007
    dp = [0] * (n + 1)
    dp[0], dp[2] = 1, 3
    extra_sum = 0  # dp[j] * 2의 누적 합

    for i in range(4, n + 1, 2):
        dp[i] = (dp[i-2] * 3 + extra_sum * 2 + 2) % MOD
        extra_sum = (extra_sum + dp[i-2]) % MOD  # 누적 합 업데이트

    return dp[n]
