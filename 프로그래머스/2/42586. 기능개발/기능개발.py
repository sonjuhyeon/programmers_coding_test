from math import ceil
from collections import deque

def solution(progresses, speeds):
    answer = []
    working_period = deque()
    
    for p, s in zip(progresses, speeds):
        rest_p = 100 - p
        working_period.append(ceil(rest_p / s))
    
    while working_period:
        deploy_day = working_period.popleft()
        answer.append(1)
        while working_period and deploy_day >= working_period[0]:
            working_period.popleft()
            answer[-1] += 1
    return answer