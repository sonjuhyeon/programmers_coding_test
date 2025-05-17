from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    dic = defaultdict(int)
    for x, y in zip(name, yearning):
        dic[x] = y
        
    for ph in photo:
        answer.append(sum([dic[p] for p in ph]))
    return answer