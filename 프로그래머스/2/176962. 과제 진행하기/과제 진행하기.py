from collections import deque
from datetime import datetime, timedelta

def solution(plans):
    answer = []
    plans.sort(key = lambda x:x[1])
    plans = deque([[p[0], datetime.strptime(p[1], "%H:%M"), int(p[2])] for p in plans])
    rest_plans = deque() # 시작한 후 중단한 과제 리스트
    
    current_time = plans[0][1] # 현재 시간
    while plans:
        sub, start_time, time_taken = plans.popleft()
        end_time = start_time + timedelta(minutes = time_taken) # 과제 종료 시간
        if plans and end_time > plans[0][1]: # 과제 종료시간이 다음 과제 시작시간 이후 일 때
            rest_plans.appendleft([sub, timedelta(minutes = time_taken) - (plans[0][1] - start_time)])
            current_time = plans[0][1]
        else:
            answer.append(sub)
            current_time = end_time
        while rest_plans and plans and current_time < plans[0][1]: # 현재 시간에서 다음과제 시작시간 사이 텀이 있을 경우
            rest_sub, rest_time = rest_plans.popleft()
            rest_end = current_time + rest_time # 남은 과제 종료 시간
            if rest_end > plans[0][1]: # 남은 과제 종료 시간이 다음 과제 시작시간 이후 일 때
                rest_time = rest_end - plans[0][1]
                rest_plans.appendleft([rest_sub, rest_time])
                current_time = plans[0][1]
            else:
                answer.append(rest_sub)
                current_time = rest_end
    
    for rest_sub, _ in rest_plans:
        answer.append(rest_sub)
    return answer