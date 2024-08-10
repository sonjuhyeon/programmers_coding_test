import math as m

def input_row(start_col, end_col, row, res):
    for i in range(start_col, end_col):
        if row >= i:
            res.append(row + 1)
        else:
            res.append(i + 1)

def solution(n, left, right):
    answer = []
    left_row = m.floor(left / n)
    right_row = m.floor(right / n)
    left_col = left % n
    right_col = right % n
    
    if left_row == right_row:
        input_row(left_col, right_col + 1, left_row, answer)
        return (answer)
    
    input_row(left_col, n, left_row, answer)
    
    for i in range(left_row + 1, right_row):
        input_row(0, n, i, answer)
                
    input_row(0, right_col + 1, right_row, answer)
        
    return answer