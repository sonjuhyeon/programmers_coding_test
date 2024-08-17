def solution(N, stages):
    challenger = [0] * (N + 2)
    for i in stages:
        challenger[i] += 1
    
    fail_ratio = {}
    total = len(stages)
    
    for i in range(1, N + 1):
        if challenger[i] == 0:
            fail_ratio[i] = 0
            continue
        fail_ratio[i] = challenger[i] / total
        total -= challenger[i]
    
    answer = sorted(fail_ratio, key = lambda x : fail_ratio[x], reverse = True)
    return answer