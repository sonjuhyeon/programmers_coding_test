from collections import deque

def solution(s):
    answer = []
    set_lst = s.split('}')
    set_lst = [deque(sl) for sl in set_lst]
    
    lst = []
    for sl in set_lst:
        tmp = []
        is_prev_digit = False
        while sl:
            val = sl.popleft()
            if val.isdigit():
                if is_prev_digit:
                    tmp[-1] += val
                else:
                    tmp.append(val)
                is_prev_digit = True
            else:
                is_prev_digit = False
        lst.append(tmp)
    lst = [[int(v) for v in ls] for ls in lst if ls]
    
    set_lst = sorted(lst, key=len)
    
    for sl in set_lst:
        for s in sl:
            if s not in answer:
                answer.append(s)
                break
    return answer