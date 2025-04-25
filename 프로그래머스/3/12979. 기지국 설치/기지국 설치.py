import math

def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1
    prev = 0  # 마지막 커버된 위치

    for st in stations:
        left = st - w
        # 이전 기지국 이후부터 현재 기지국 전파 시작 전까지 커버 안 된 구간 길이
        uncovered = max(0, left - prev - 1)
        answer += math.ceil(uncovered / coverage)
        prev = st + w  # 현재 기지국이 커버하는 끝 지점

    # 마지막 기지국 이후 남은 구간 처리
    if prev < n:
        answer += math.ceil((n - prev) / coverage)

    return answer
