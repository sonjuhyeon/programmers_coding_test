def check_open_bracket(char):
    if char == '[' or char == '{' or char == '(':
        return 1
    else:
        return 0

def check_bracket(sub):
    ret = 0
    stack = []
    for i in range(len(sub)):
        if not stack:
            if check_open_bracket(sub[i]):
                stack.append(sub[i])
                continue
            else:
                return 0
        if (check_open_bracket(sub[i])):
            stack.append(sub[i])
            continue
        else:
            if (
                stack[-1] == '[' and sub[i] == ']' or
                stack[-1] == '{' and sub[i] == '}' or
                stack[-1] == '(' and sub[i] == ')'
            ):
                stack.pop()
            else:
                return 0
    return 1

def solution(s):
    len_s = len(s)
    if (len_s % 2 == 1):
        return 0
    
    double_s = s * 2
    answer = 0
    for i in range(len_s):
        sub = double_s[i:i + len_s]
        answer += check_bracket(sub)
    return answer