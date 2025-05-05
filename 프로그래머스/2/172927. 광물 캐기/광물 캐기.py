from itertools import permutations

def solution(picks, minerals):
    fatigue_table = {
        'diamond': [1, 5, 25],  # [다이아곡, 철곡, 돌곡]
        'iron': [1, 1, 5],
        'stone': [1, 1, 1]
    }

    groups = []
    for i in range(0, len(minerals), 5):
        group = minerals[i:i+5]
        if len(groups) < sum(picks):  # 사용할 수 있는 곡괭이 수까지만 그룹핑
            groups.append(group)
        else:
            break
    
    group_infos = []
    for group in groups:
        dia, iron, stone = 0, 0 , 0
        for m in group:
            dia += fatigue_table[m][0]
            iron += fatigue_table[m][1]
            stone += fatigue_table[m][2]
        group_infos.append((dia, iron, stone))
        
    tools = []
    for pick_type, count in enumerate(picks):
        tools.extend([pick_type] * count)
    tools = tools[:len(groups)]  # 그룹 수만큼만 자르기
    
    perm_tools = permutations(tools, len(tools))
    answer = []
    
    for tool in perm_tools:
        fatigue = 0
        for t, info in zip(tool, group_infos):
            fatigue += info[t]
        answer.append(fatigue)
        
    return min(answer)