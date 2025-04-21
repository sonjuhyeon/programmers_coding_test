from collections import defaultdict

def solution(survey, choices):
    personality = defaultdict(int)
    for sv, choice in zip(survey, choices):
        if choice <= 3:
            if choice == 1:
                personality[sv[0]] += 3
            elif choice == 2:
                personality[sv[0]] += 2
            else:
                personality[sv[0]] += 1
        elif choice >= 5:
            if choice == 5:
                personality[sv[1]] += 1
            elif choice == 6:
                personality[sv[1]] += 2
            else:
                personality[sv[1]] += 3
    # print(personality)
    
    answer = ''
    if personality['R'] >= personality['T']:
        answer += 'R'
    else:
        answer += 'T'
    if personality['C'] >= personality['F']:
        answer += 'C'
    else:
        answer += 'F'
    if personality['J'] >= personality['M']:
        answer += 'J'
    else:
        answer += 'M'
    if personality['A'] >= personality['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer