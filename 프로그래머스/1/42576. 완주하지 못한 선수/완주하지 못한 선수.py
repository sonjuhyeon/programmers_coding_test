def solution(participant, completion):
    players_dic = {}
    players = set(participant)
    for player in players:
        players_dic[player] = 0
        
    for player in participant:
        players_dic[player] += 1
        
    for player in completion:
        if player in players_dic:
            players_dic[player] -= 1
            
    for player in players_dic:
        if players_dic[player] == 1:
            answer = player
            break

    return answer