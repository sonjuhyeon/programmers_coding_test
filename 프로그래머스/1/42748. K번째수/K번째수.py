def solution(array, commands):
    answer = []
    for i, j, k in commands:
        lst = sorted(array[i-1:j])
        answer.append(lst[k-1])
    return answer