def solution(board, moves):
    answer = 0
    a = 0
    b = []
    lis = []
    for i in moves:
        for j in range(len(board)):
            if board[a][i-1] != 0:
                b.append(board[a][i-1])
                board[a][i-1] = 0
                a = 0
                break
            elif board[a][i-1] == 0:
                a += 1
                if a >= len(board):
                    a = 0
                    break    

    for k in b:        
        if len(lis) == 0:
            lis.append(k)
        elif lis[-1] == k:
            lis.pop()  
            answer += 2
        elif lis[-1] != k:
            lis.append(k)

    return answer
