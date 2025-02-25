from collections import Counter
def solution(X, Y):

    x_count = Counter(X)  # X의 숫자 개수 카운트
    y_count = Counter(Y)  # Y의 숫자 개수 카운트

    answer_lst = []

    # 0~9 숫자에 대해 최소 등장 횟수만큼 추가
    for digit in range(9, -1, -1):  # 내림차순 정렬을 위해 9부터 0까지 탐색
        digit = str(digit)
        if digit in x_count and digit in y_count:
            answer_lst.append(digit * min(x_count[digit], y_count[digit]))

    if not answer_lst:
        return "-1"

    answer = "".join(answer_lst)
    return "0" if answer[0] == "0" else answer
