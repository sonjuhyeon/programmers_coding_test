from collections import defaultdict

def solution(survey, choices):
    personality = defaultdict(int)
    for sv, choice in zip(survey, choices):
        if choice <= 3:
            personality[sv[0]] += 4 - choice
        elif choice >= 5:
            personality[sv[1]] += choice - 4
    
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