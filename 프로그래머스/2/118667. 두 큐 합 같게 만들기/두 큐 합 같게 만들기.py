from collections import deque

def solution(queue1, queue2):
    answer = 0
    len_que = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total1 = sum(queue1)
    total2 = sum(queue2)
    
    while answer <= (len_que * 3):
        if total1 == total2:
            return answer
        elif total1 > total2:
            val = queue1.popleft()
            queue2.append(val)
            total1 -= val
            total2 += val
        else:
            val = queue2.popleft()
            queue1.append(val)
            total1 += val
            total2 -= val
        answer += 1
    
    return -1

[1, 1, 1, 1]
[1, 1, 7, 1]
answer : 9