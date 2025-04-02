def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    x = -1 # 요격 위치
    
    for s, e in targets:
        if x < s:
            answer += 1
            x = e - 0.5
    return answer