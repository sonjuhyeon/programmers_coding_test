def solution(players, callings):
    players_dic = {}
    for i, player in enumerate(players):
        players_dic[player] = i
    for call in callings:
        idx = players_dic[call]
        prev_player = players[idx - 1]
        curr_player = players[idx]
        players[idx - 1] = curr_player
        players[idx] = prev_player
        
        players_dic[curr_player] -= 1
        players_dic[prev_player] += 1
    answer = players
    return answer
