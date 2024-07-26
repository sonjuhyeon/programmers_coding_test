def solution(board, h, w):
    answer = 0
    
    directions = []#up, down, left, right
    size = len(board)
    value = board[h][w]
    
    directions.append([h-1, w])
    directions.append([h+1, w])
    directions.append([h, w-1])
    directions.append([h, w+1])
    print(directions)
    #up
    if (h-1 >= 0):
        if board[directions[0][0]][directions[0][1]] == value:
            answer += 1
    
    #left
    if (w-1 >= 0):
        if board[directions[2][0]][directions[2][1]] == value:
            answer += 1
    #down
    if (h+1 < size):
        if board[directions[1][0]][directions[1][1]] == value:
            answer += 1
    
    #right
    if (w+1 < size):
        if board[directions[3][0]][directions[3][1]] == value:
            answer += 1
    
    return answer