def solution(number, k):
    stack = []
    for i, num in enumerate(number):
        # 스택의 마지막 값이 현재 값보다 작으면 스택에서 제거 (k 감소)
        while stack and (stack[-1] < num) and (k > 0):
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 만약 k가 남아있다면 뒤에서부터 제거
    if k > 0:
        stack = stack[:-k]
    
    # 리스트를 문자열로 합쳐서 반환
    answer = ''.join(stack)
    return answer
