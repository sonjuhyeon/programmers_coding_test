from collections import defaultdict

def solution(keymap, targets):
    answer = []
    keypad = defaultdict(int)
    for km in keymap:
        for i, char in enumerate(km):
            if keypad[char] == 0:
                keypad[char] = i + 1
            else:
                if keypad[char] > i:
                    keypad[char] = i + 1
    for target in targets:
        count = 0
        for char in target:
            count += keypad[char]
            if keypad[char] == 0:
                answer.append(-1)
                break
        else:
            answer.append(count)
    return answer