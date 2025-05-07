def solution(arr):
    answer = 0
    arr = ''.join(arr).split('-')
    
    min_tail, max_tail = 0, 0
    for i in range(len(arr) - 1, -1, -1):
        tmp = list(map(int, arr[i].split('+')))
        if i != 0:
            min_tmp = -sum(tmp)
            max_tmp = -2 * tmp[0] + sum(tmp)
            min_tail, max_tail = (
                min(min_tmp + min_tail, min_tmp - max_tail),
                max(max_tmp + max_tail, min_tmp - min_tail)
            )
        else:
            for n in tmp:
                answer += n
    answer += max_tail
    return answer