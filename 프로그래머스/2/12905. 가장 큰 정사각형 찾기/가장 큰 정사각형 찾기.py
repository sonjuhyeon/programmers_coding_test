def solution(board):
    row_n = len(board)
    col_n = len(board[0])

    # DP 테이블 초기화 (board와 같은 크기)
    dp = [[0] * col_n for _ in range(row_n)]

    # 첫 행과 첫 열은 그대로 사용
    for i in range(row_n):
        dp[i][0] = board[i][0]
    for j in range(col_n):
        dp[0][j] = board[0][j]
    
    # 동적 계획법으로 최대 정사각형 크기 계산
    for i in range(1, row_n):
        for j in range(1, col_n):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    return max([max(row) for row in dp]) ** 2
