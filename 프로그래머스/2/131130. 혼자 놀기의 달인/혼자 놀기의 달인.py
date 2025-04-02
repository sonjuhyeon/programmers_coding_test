def solution(cards):
    visited = []
    cards = [n - 1 for n in cards]
    cycle_lst = []
    
    for i in range(len(cards)):
        cur_idx = i
        if i in visited:
            continue
        else:
            cnt = 0
            while cur_idx not in visited:
                visited.append(cur_idx)
                cur_idx = cards[cur_idx]
                cnt += 1
            cycle_lst.append(cnt)
            
    if len(cycle_lst) < 2:
        return 0  # 사이클이 1개 이하일 경우 점수는 0
    
    cycle_lst.sort()
    answer = cycle_lst[-1] * cycle_lst[-2]
    return answer