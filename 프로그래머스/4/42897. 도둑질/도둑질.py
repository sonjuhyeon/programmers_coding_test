def solution(money):
    N = len(money)
    dp1 = [0 for _ in range(N - 1)]
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, N - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
        
    dp2 = [0 for _ in range(N)]
    dp2[1] = money[1]
    for i in range(2, N):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
        
    return max(dp1[-1], dp2[-1])