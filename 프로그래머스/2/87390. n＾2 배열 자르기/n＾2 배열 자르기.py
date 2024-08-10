import math as m

def solution(n, left, right):
    answer = []
    left_row = m.floor(left / n)
    right_row = m.floor(right / n)
    left_col = left % n
    right_col = right % n
    
    if left_row == right_row:
        for i in range(left_col, right_col + 1):
            if left_row >= i:
                answer.append(left_row + 1)
            else:
                answer.append(i + 1)
        return (answer)
    
    for i in range(left_col, n):
        if left_row >= i:
            answer.append(left_row + 1)
        else:
            answer.append(i + 1)
    
    for i in range(left_row + 1, right_row):
        for j in range(n):
            if j <= i:
                answer.append(i + 1)
            else:
                answer.append(j + 1)
                
    for i in range(right_col + 1):
        if i <= right_row:
            answer.append(right_row + 1)
        else:
            answer.append(i + 1)
        
    return answer