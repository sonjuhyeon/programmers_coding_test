def solution(s):
    answer = 0
    x_cnt = 0
    non_x_cnt = 0
    x = s[0]

    for idx, char in enumerate(s):
        if char == x:
            x_cnt += 1
        else:
            non_x_cnt +=1

        if idx == len(s)-1:
            answer += 1
        elif x_cnt == non_x_cnt: 
            answer += 1
            x_cnt, non_x_cnt = 0, 0
            x = s[idx+1]

    return answer