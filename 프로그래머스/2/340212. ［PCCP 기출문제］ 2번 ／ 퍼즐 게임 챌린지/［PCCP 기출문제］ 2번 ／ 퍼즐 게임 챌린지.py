def solution(diffs, times, limit):
    max_level, min_level = max(diffs), 1  # 최대 레벨, 최소 레벨을 설정

    while min_level < max_level:
        # 중간 지점을 설정
        mid_level = (min_level + max_level) // 2
        mid_total = 0

        for i in range(len(diffs)):
            if not i:
                time_prev = 0
            else:
                time_prev = times[i - 1]

            time_cur = times[i] # 현재 문제에 필요한 시간
            
            if mid_level >= diffs[i]: # 숙련도가 난이도보다 높을 때
                mid_total += time_cur
            else: # 숙련도가 난이도보다 낮을 때
                mid_total += (diffs[i] - mid_level) * (time_cur + time_prev) + time_cur
    
        if mid_total <= limit: # 중간 레벨이 제한 시간 내에 문제를 풀 수 있다면
            max_level = mid_level # 최댓값을 내림
        else: # 제한 시간 내에 문제를 풀 수 없다면
            min_level = mid_level + 1 # 최솟값을 올림

    return min_level