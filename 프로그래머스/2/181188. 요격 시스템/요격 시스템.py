def solution(targets):
    answer = 0
    targets.sort(reverse=True)
    x = max([target[1] for target in targets]) # 요격 위치
    
    for s, e in targets:
        if x >= e:
            answer += 1
            x = s + 0.5
    return answer