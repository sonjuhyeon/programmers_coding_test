def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)  # 마지막 거리까지 포함
    left, right = 1, distance
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        delete_rocks = 0
        prev_rock = 0  # 이전 바위 위치

        for rock in rocks:
            if rock - prev_rock < mid:  # 거리(mid)보다 작으면 돌을 제거
                delete_rocks += 1
                if delete_rocks > n:
                    break
            else:
                prev_rock = rock  # 돌을 유지함

        if delete_rocks > n:
            right = mid - 1  # 거리를 줄여야 함
        else:
            answer = mid  # 현재 mid를 저장
            left = mid + 1  # 거리를 늘려서 더 큰 값 탐색

    return answer
