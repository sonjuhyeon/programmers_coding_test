def solution(m, n, puddles):
    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 출발점
    
    # 물 웅덩이 위치를 Set으로 변환 (빠른 조회)
    puddles = set((x, y) for x, y in puddles)

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j, i) == (1, 1):  # 출발점은 이미 1로 설정
                continue
            if (j, i) in puddles:  # 물웅덩이 있는 곳은 지나갈 수 없음
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])

    return dp[n][m]  % 1_000_000_007 # 도착점의 경로 개수 반환
