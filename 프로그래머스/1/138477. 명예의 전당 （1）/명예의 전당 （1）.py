def solution(k, score):
    answer = []
    top3 = []

    for idx, num in enumerate(score):
        if idx < k:
            top3.append(num)
        elif top3[-1] < num:
            top3[-1] = num

        top3 = sorted(top3, reverse=True)
        answer.append(top3[-1])

    return answer