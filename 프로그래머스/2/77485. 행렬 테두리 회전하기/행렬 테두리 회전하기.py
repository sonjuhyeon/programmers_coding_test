def rotate(matrix, row1, col1, row2, col2):
    top_numbers = matrix[row1][col1:col2]  # 상단 행 추출 (오른쪽 제외)
    bottom_numbers = matrix[row2][col1+1:col2+1]  # 하단 행 추출 (왼쪽 제외)
    left_numbers = [matrix[r][col1] for r in range(row1+1, row2+1)]  # 왼쪽 열 추출 (상단 제외)
    right_numbers = [matrix[r][col2] for r in range(row1, row2)]  # 오른쪽 열 추출 (하단 제외)
    
    min_n=min(top_numbers + bottom_numbers + left_numbers + right_numbers) # 최소값
    
    # print(top_numbers, bottom_numbers, left_numbers, right_numbers)
    matrix[row1][col1+1:col2+1] = top_numbers # 상단행 오른쪽으로 한칸 이동
    matrix[row2][col1:col2] = bottom_numbers # 하단행 왼쪽으로 한칸 이동
    
    # 왼쪽열 위로 한칸 이동
    for r in range(row1, row2):  
        matrix[r][col1] = left_numbers[r - row1]
        
    # 오른쪽열 아래로 한칸 이동
    for r in range(row1 + 1, row2 + 1):
        matrix[r][col2] = right_numbers[r - row1 - 1]
    
    
    return matrix, min_n

def solution(rows, columns, queries):
    answer = []
    
    matrix = [[col + row * columns for col in range(1, columns + 1)] for row in range(rows)]
    for row1, col1, row2, col2 in queries:
        row1, col1, row2, col2 = row1 - 1, col1 - 1, row2 - 1, col2 - 1
        matrix, min_n = rotate(matrix, row1, col1, row2, col2)
        answer.append(min_n)
        
    return answer