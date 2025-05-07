def solution(arr):
    answer = 0
    arr = ''.join(arr).split('-')
    
    min_tail, max_tail = 0, 0
    for i in range(len(arr) - 1, -1, -1):
        tmp = arr[i].split('+')
        if i != 0:
            min_tmp = sum([-int(n) for n in tmp])
            max_tmp = sum([int(n) if i >= 1 else -int(n) for i, n in enumerate(tmp)])
            if i == len(arr) - 1:
                min_tail = min_tmp
                max_tail = max_tmp
            else:
                min_tail, max_tail = min(min_tmp + min_tail, min_tmp - max_tail), max(max_tmp + max_tail, min_tmp - min_tail)
        else:
            for n in tmp:
                answer += int(n)
    answer += max_tail
    return answer