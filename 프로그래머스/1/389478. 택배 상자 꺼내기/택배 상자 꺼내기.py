def solution(n, w, num):
    answer = 0
    while (num <= n):
        print(num)
        if (num - 1 % w) == 0:
            num += 2 * (w - ((num - 1) % w)) - 1
        else:
            num += 2 * (w - ((num - 1) % w)) - 1
        answer += 1
    return answer