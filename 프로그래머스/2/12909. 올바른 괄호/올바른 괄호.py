from collections import deque

def solution(s):
    dq = deque(s)
    check_s = deque()
    
    while dq:
        if '(' == dq.popleft():
            check_s.append('(')
        else:
            if check_s:
                check_s.popleft()
            else:
                return False
    
    if check_s:
        return False
    return True