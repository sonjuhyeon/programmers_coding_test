import math as m

def solution(r1, r2):
    answer = 0
    
    for i in range(1, r2 + 1):
        y2 = m.floor(m.sqrt(r2 * r2 - i * i))
        if (i < r1):
            y1 = m.ceil(m.sqrt(r1 * r1 - i * i))
            answer += (y2 - y1 + 1)
        else:
            answer += (y2 + 1)
    answer *= 4

    return answer