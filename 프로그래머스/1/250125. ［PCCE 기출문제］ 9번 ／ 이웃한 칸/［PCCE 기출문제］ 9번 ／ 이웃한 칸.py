def solution(board, h, w):
    answer = 0
    board_size = len(board)
    dh = [0, 1, 0, -1] # row 변화
    dw = [1, 0, -1, 0] # col 변화
    
    for row, col in zip(dh, dw):
        current_row = h + row
        current_col = w + col
        
        if (0 <= current_row < board_size) and (0 <= current_col < board_size):
            if board[h][w] == board[current_row][current_col]:
                answer += 1
    return answer