def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        max_y = (d ** 2 - x ** 2) ** 0.5
        cnt_y = int(max_y // k) + 1
        answer += cnt_y
    return answer