def count_people_processed(mid_time, times): # 주어진 시간동안 처리할수 있는 사람 수
    res = 0
    for time in times:
        res += mid_time // time
    return res
    
def solution(n, times):
    times.sort()
    min_time = times[0]
    max_time = times[0] * n

    while min_time <= max_time:
        mid_time = (max_time + min_time) // 2 # 중간 시간 계산

        if count_people_processed(mid_time, times) >= n:
            max_time = mid_time - 1 # mid_time으로도 n명을 처리할 수 있으므로 더 작은 값 탐색
        else:
            min_time = mid_time + 1 # mid_time으로 n명을 처리할 수 없으므로 더 큰 값 탐색

    return min_time