def solution(bandage, health, attacks):
    answer = 0
    attk_len = len(attacks)
    attk_time_list = []
    suc_time = -1
    init_health = health
    
    for i in range(attk_len):
        attk_time_list.append(attacks[i][0])
    
    last_attk_time = attk_time_list[attk_len - 1]
    
    for i in range(last_attk_time + 1):
        if i in attk_time_list:
            for j in range(len(attacks)):
                if i == attacks[j][0]:
                    health -= attacks[j][1]
                    suc_time = 0
                    if health <= 0:
                        return (-1)
        else:
            suc_time += 1
            health += bandage[1]
            if bandage[0] == suc_time:
                suc_time = 0
                health += bandage[2]
            if health >= init_health:
                health = init_health
    
    answer = health    
    return answer