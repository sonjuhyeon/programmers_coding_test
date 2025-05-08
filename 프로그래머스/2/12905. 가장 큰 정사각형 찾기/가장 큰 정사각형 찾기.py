def solution(board):
    row_n = len(board)
    col_n = len(board[0])
    
    # 동적 계획법으로 최대 정사각형 크기 계산
    for i in range(1, row_n):
        for j in range(1, col_n):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    return max([max(row) for row in board]) ** 2
