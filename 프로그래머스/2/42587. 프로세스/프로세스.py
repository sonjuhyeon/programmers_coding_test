from collections import deque

def solution(priorities, location):
    priorities = deque((priority, i) for i, priority in enumerate(priorities))
    max_priority = max(priorities, key=lambda x: x[0])[0]  # 현재 가장 높은 우선순위

    answer = 0
    while priorities:
        now = priorities.popleft()
        
        # 현재 문서가 가장 높은 우선순위인지 확인
        if now[0] == max_priority:
            answer += 1
            if now[1] == location:  # 찾는 문서라면 반환
                return answer
            # 최대 우선순위를 다시 계산
            if priorities:
                max_priority = max(priorities, key=lambda x: x[0])[0]
        else:
            priorities.append(now)  # 우선순위가 낮으면 다시 큐에 삽입
