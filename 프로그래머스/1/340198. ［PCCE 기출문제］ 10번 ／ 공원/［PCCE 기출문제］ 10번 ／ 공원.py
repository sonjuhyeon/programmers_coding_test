def check_sq(max_size, park, row, col):
    # print(f"({row}, {col})")
    
    for size in range(1, max_size + 1):
        end = size - 1
        
        # 가장 오른쪽 열 확인
        for i in range(end):
            if park[row + i][col + end] != '-1':
                return end
            # print(f"좌표: ({row + i}, {col + end}), 값: {park[row + i][col + end]}")
        
        # 가장 아래쪽 행 확인
        for i in range(end, -1, -1):
            if park[row + end][col + i] != '-1':
                return end
            # print(f"좌표: ({row + end}, {col + i}), 값: {park[row + end][col + i]}")
    return max_size

def solution(mats, park):
    square = []
    ans_list = []
    row = 0,
    col = 0
    
    x_size = len(park[0])
    y_size = len(park)
    
    for c in range(0, x_size):
        for r in range(0, y_size):
            if park[r][c] == '-1':
                max_size = min(x_size - c, y_size - r) # 현 위치에서 가장 큰 정사각형 크기
                square.append(check_sq(max_size, park, r, c))
    
    max_sq = max(square)
    for m in mats:
        if m <= max_sq:
            ans_list.append(m)
    
    if ans_list:
        return max(ans_list)
    else:
        return -1