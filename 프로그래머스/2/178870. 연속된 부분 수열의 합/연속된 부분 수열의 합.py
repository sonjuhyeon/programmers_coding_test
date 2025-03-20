def solution(sequence, k):
    left, right = 0, 0
    curr_sum = sequence[0]  # 현재 부분 배열의 합
    answer = []

    while right < len(sequence):
        if curr_sum == k:
            answer.append([left, right])

        if curr_sum < k:
            right += 1
            if right < len(sequence):
                curr_sum += sequence[right]
        else:
            curr_sum -= sequence[left]
            left += 1
    
    # 가장 짧은 구간 선택
    return min(answer, key=lambda x: (x[1] - x[0], x[0])) if answer else []
