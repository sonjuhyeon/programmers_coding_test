def solution(k, ranges):
    answer = []
    collatz_conjecture = []
    collatz_conjecture.append(k)
    while (k > 1):
        if (k % 2 == 0):
            k /= 2
            collatz_conjecture.append(k)
        else:
            k = k * 3 + 1
            collatz_conjecture.append(k)
    
    for integration in ranges:
        area = 0
        cc_len = len(collatz_conjecture)
        start_idx = integration[0]
        end_idx = cc_len + integration[1] - 1
        if (start_idx > end_idx):
            answer.append(-1)
        elif (start_idx == end_idx):
            answer.append(0)
        else:
            for i in range(start_idx, end_idx):
                area += (collatz_conjecture[i] + collatz_conjecture[i + 1]) / 2
            answer.append(area)
    return answer