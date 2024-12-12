def is_opening_bracket(char):
    return char in '({['  # 여는 괄호인지 확인

def is_balanced_brackets(substring):
    stack = []
    for char in substring:
        if is_opening_bracket(char):
            stack.append(char)  # 여는 괄호는 스택에 추가
        elif stack and (
            (stack[-1] == '[' and char == ']') or
            (stack[-1] == '{' and char == '}') or
            (stack[-1] == '(' and char == ')')
        ):
            stack.pop()  # 닫는 괄호가 맞으면 스택에서 제거
        else:
            return False  # 잘못된 괄호가 있으면 균형이 맞지 않음
    return not stack  # 스택이 비어 있으면 괄호가 균형을 이룸

def solution(s):
    n = len(s)
    if n % 2 == 1:  # 문자열 길이가 홀수이면 균형을 맞출 수 없음
        return 0
    
    doubled_s = s * 2  # 문자열을 두 배로 늘려 회전된 문자열을 시뮬레이션
    
#     answer = 0
#     for i in range(n):
#         substring = doubled_s[i:i + n]
#         answer += is_balanced_brackets(substring)
#     return answer
    return sum(is_balanced_brackets(doubled_s[i:i + n]) for i in range(n))