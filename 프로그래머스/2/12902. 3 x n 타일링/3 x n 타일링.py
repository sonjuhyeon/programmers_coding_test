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
