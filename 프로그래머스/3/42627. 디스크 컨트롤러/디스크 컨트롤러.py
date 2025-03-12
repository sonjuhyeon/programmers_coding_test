from heapq import heappop, heappush
from collections import deque

def solution(jobs):
    jobs = deque(sorted(jobs))
    
    current_time = 0  # 현재 시간
    heap = []  # 실행 대기 큐 (최소 힙)
    turnaround_time = []  # 각 작업의 총 대기 시간 리스트
    
    while jobs or heap:
        # 현재 시간 기준으로 실행할 수 있는 작업을 heap에 추가
        while jobs and jobs[0][0] <= current_time:
            work_request_time, run_time = jobs.popleft()
            heappush(heap, (run_time, work_request_time))  # 실행 시간이 우선순위

        if heap:
            # 실행 시간이 가장 짧은 작업을 실행
            run_time, work_request_time = heappop(heap)
            current_time += run_time
            turnaround_time.append(current_time - work_request_time)
        else:
            # 실행할 수 있는 작업이 없으면 현재 시간을 가장 빠른 도착 시간으로 업데이트
            current_time = jobs[0][0]

    # 평균 대기 시간 반환
    return sum(turnaround_time) // len(turnaround_time)
