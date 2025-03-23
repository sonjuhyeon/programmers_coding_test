def time_to_solve(level, diff, time_cur, time_prev):
    # 숙련도가 난이도보다 높을 때
    if level >= diff:
        return time_cur
    # 숙련도가 난이도보다 낮을 때
    else:
        return (diff - level) * (time_cur + time_prev) + time_cur

def solution(diffs, times, limit):
    # 최대 레벨, 최소 레벨을 설정합니다.
    max_level, min_level = max(diffs), 1

    # 최소 레벨이 최대 레벨과 같아질 때까지 반복합니다.
    while min_level < max_level:
        # 중간 지점을 설정합니다.
        mid_level = (min_level + max_level) // 2
        mid_total = 0

        # 모든 난이도에 대해 탐색합니다.
        for i in range(len(diffs)):
            # 처음 위치에만 time_prev가 0
            if not i:
                time_prev = 0
            else:
                time_prev = times[i - 1]

            # 현재 문제에 필요한 시간
            time_cur = times[i]
            mid_total += time_to_solve(mid_level, diffs[i], time_cur, time_prev)

        # 중간 레벨이 제한 시간 내에 문제를 풀 수 있다면
        # 최댓값을 내려줍니다.
        if mid_total <= limit:
            max_level = mid_level
        # 제한 시간 내에 문제를 풀 수 없다면
        # 최솟값을 올려줍니다.
        else:
            min_level = mid_level + 1

    # 최소 레벨을 반환합니다.
    return min_level