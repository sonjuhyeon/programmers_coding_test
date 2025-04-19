def solution(arr):
    answer = []
    for num in arr:
        if answer:
            if answer[-1] == num:
                continue
            else:
                answer.append(num)
        else:
            answer.append(num)
    return answer