from collections import deque

def solution(dartResult):
    answer = []
    idx = -1
    dartResult = deque(dartResult)
    
    while dartResult:
        score = ''
        char = dartResult.popleft()
        while char.isdigit():
            score += char
            char = dartResult.popleft()
        if score:
            answer.append(int(score))
            idx += 1
        if char == 'S':
            pass
        elif char == 'D':
            answer[idx] **= 2
        elif char == 'T':
            answer[idx] **= 3
        elif char == '*':
            answer[idx] *= 2
            if idx != 0:
                answer[idx - 1] *= 2
        elif char == '#':
            answer[idx] *= -1
    return sum(answer)