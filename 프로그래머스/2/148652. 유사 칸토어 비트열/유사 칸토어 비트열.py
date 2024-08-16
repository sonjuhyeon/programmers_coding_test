def solution(n, l, r):
    answer = 0
    for i in range(l - 1, r):
        j = i
        while j > 0:
            j, mod = divmod(j, 5)
            if mod == 2:
                break
        else:
            answer += 1
    return answer