def get_max_lst(now_level, next_level):
    res = [0] * len(next_level)
    for i in range(len(next_level)):
        if i == 0:
            res[i] = next_level[i] + now_level[i]
        elif i == len(next_level) - 1:
            res[i] = next_level[i] + now_level[i - 1]
        else:
            left = next_level[i] + now_level[i - 1]
            right = next_level[i] + now_level[i]
            if left > right:
                res[i] = left
            else:
                res[i] = right
    return (res)

def solution(triangle):
    tri_len = len(triangle)
    answer_lst = triangle[0]
    for level in range(1, tri_len):
        answer_lst = get_max_lst(answer_lst, triangle[level])
    answer = max(answer_lst)
    return answer