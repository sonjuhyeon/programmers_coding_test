def solution(s):
    answer = True
    stack = []
    
    for char in s:
        if stack:
            if char == '(':
                stack.append(char)
            else:
                stack.pop()
        else:
            stack.append(char)
    return False if stack else True