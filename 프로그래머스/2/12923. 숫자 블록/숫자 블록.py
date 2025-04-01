def get_max_divisor(num):
            
    # 1은 약수가 없으므로 0
    if num == 1:
        return 0

    # 2부터 sqrt(num)까지 검사
    res = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            div = num // i
            if div <= 10_000_000:
                return div
            else:
                res = i
                continue
    return res


def solution(begin, end):
    return [get_max_divisor(num) for num in range(begin, end + 1)]