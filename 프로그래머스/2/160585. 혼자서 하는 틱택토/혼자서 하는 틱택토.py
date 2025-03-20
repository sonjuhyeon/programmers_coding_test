def who_won(board):
    win_lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    o = []
    x = []

    for idx1, val1 in enumerate(board):
        for idx2, val2 in enumerate(val1):
            if val2 == 'O':
                o.append(win_lines[idx1][idx2])
            elif val2 == 'X':
                x.append(win_lines[idx1][idx2])

    player_o = [sublist for sublist in win_lines if all(num in o for num in sublist)]
    player_x = [sublist for sublist in win_lines if all(num in x for num in sublist)]
    
    return [bool(player_o), bool(player_x)]
    

def solution(board):
    count_o = sum([row.count('O') for row in board])
    count_x = sum([row.count('X') for row in board])
    win_player = who_won(board)
    print(win_player)
    
    if (count_x > count_o or # 후 플레이어가 수를 더 많이 두었을 경우
        count_o - count_x >= 2 or # 선 플레이어가 후 플레이어보다 두수 이상 더 많이 두었을 경우
        (win_player[0] and win_player[1]) or # 두 플레이어 모두 승리한 경우
        (win_player[0] and count_o == count_x) or # 선 플레이어가 승리하였는데 후 플레이어가 이후 수를 둔 경우
        (win_player[1] and count_o > count_x) # 후 플레이어가 승리하였는데 선 플레이어가 이후 수를 둔 경우
       ):
        return 0
    

    answer = 1
    return answer