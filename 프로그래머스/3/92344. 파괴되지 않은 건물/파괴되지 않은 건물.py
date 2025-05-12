def solution(board, skill):
    row_n, col_n = len(board), len(board[0])
    # 누적합 기록을 위한 임시 배열 (row_n+1, col_n+1 크기)
    acc = [[0] * (col_n + 1) for _ in range(row_n + 1)]
    
    # 스킬 효과 기록
    for skill_type, r1, c1, r2, c2, degree in skill:
        effect = -degree if skill_type == 1 else degree
        acc[r1][c1] += effect
        acc[r1][c2 + 1] -= effect
        acc[r2 + 1][c1] -= effect
        acc[r2 + 1][c2 + 1] += effect
        
    # 행 기준으로 누적합 계산
    for i in range(row_n):
        for j in range(1, col_n):
            acc[i][j] += acc[i][j - 1]
            
    # 열 기준으로 누적합 계산
    for j in range(col_n):
        for i in range(1, row_n):
            acc[i][j] += acc[i - 1][j]
            
    # 누적합을 원래 보드에 더하여 파괴되지 않은 건물 수 계산
    answer = 0
    for i in range(row_n):
        for j in range(col_n):
            board[i][j] += acc[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
