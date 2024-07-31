def solution(arr1, arr2):
    row1 = len(arr1)
    col1 = len(arr1[0])
    row2 = len(arr2)
    col2 = len(arr2[0])
    
    answer = []
    for i in range(row1):
        answer.append([0] * col2)
        
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer