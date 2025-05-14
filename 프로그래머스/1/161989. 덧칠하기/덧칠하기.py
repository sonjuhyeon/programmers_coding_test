def solution(n, m, section):
    section.sort()
    answer = 0
    current_position = 0 

    for s in section:
        if s > current_position:
            answer += 1
            current_position = s + m - 1

    return answer
