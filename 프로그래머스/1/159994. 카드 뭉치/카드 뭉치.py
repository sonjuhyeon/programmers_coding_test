def solution(cards1, cards2, goal):
    answer = ''
    idx1 = 0
    idx2 = 0
    for word in goal:
        if idx1 < len(cards1) and word == cards1[idx1]:
            idx1 += 1
        if idx2 < len(cards2) and word == cards2[idx2]:
            idx2 += 1
    if len(goal) == idx1 + idx2:
        answer = 'Yes'
    else:
        answer = "No"
    return answer