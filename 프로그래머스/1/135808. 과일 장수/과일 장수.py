def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    mod = len(score) % m
    if mod:
        score = score[:-mod]
        
    for i in range(0, len(score), m):
        box = score[i:i+m]
        answer += min(box) * m
    return answer