def solution(answers):
    supojas = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0, 0, 0]
    for i, answer in enumerate(answers):
        for j, supoja in enumerate(supojas):
            if (answer == supoja[i % len(supoja)]):
                scores[j] += 1
    max_score = max(scores)
    answer = []
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)
    return answer