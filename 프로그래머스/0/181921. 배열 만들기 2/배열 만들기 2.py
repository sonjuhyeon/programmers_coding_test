def solution(l, r):
    answer = []
    l_digit = len(str(l))
    r_digit = len(str(r))
    arr = []
    
    for i in range(l_digit):
        tmp = (10 ** i) * 5
        arr.append(tmp)
        for j in range(2 ** i - 1):
            arr.append(tmp + arr[j])
    
    for i in range(l_digit - 1, r_digit):
        tmp = (10 ** i) * 5
        if tmp > r:
            break
        if tmp >= l:
            answer.append(tmp)
        union = sorted(list(set(answer) | set(arr)))
        for j in range(2 ** i - 1):
            if (tmp + union[j]) > r:
                break
            if (tmp + union[j]) >= l:
                answer.append(tmp + union[j])
    
    if not(answer):
        return [-1]
    
    return answer