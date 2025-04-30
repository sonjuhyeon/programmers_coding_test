from collections import deque

def solution(s):
    answer = ''
    s = deque(s)
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
               'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    while s:
        num = s.popleft()
        if num.isdigit():
            answer += num
        else:
            while num not in numbers:
                num += s.popleft()
            answer += str(numbers[num])
            
    return int(answer)