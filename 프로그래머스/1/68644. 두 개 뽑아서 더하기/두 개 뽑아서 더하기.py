def solution(numbers):
    tmp = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            tmp.append(numbers[i] + numbers[j])
    answer = sorted(set(tmp))
    return answer