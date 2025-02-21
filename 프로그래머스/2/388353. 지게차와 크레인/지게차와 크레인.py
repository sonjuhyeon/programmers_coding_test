from collections import deque

def check_outside(storage, row, col):
    """BFS를 이용해 특정 위치와 그 주변이 외부와 연결되었는지 확인 후 0으로 변환"""
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    row_len, col_len = len(storage), len(storage[0])
    queue = deque([(row, col)])
    visited = set([(row, col)])
    connected_cells = [(row, col)]
    is_outside = False  # 외부와 연결 여부 확인

    while queue:
        r, c = queue.popleft()

        # 경계에 위치한 경우 또는 주변에 0이 있으면 외부와 연결된 것으로 판단
        if r == 0 or r == row_len - 1 or c == 0 or c == col_len - 1:
            is_outside = True
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < row_len and 0 <= nc < col_len: # out of range check
                if storage[nr][nc] == 0:
                    is_outside = True  # 외부와 연결됨
                elif storage[nr][nc] == 1 and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    connected_cells.append((nr, nc))  # 연결된 1 저장

    # 외부와 연결된 경우만 0으로 변환
    if is_outside:
        for r, c in connected_cells:
            storage[r][c] = 0

def crane(storage, req):
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] == req:
                storage[i][j] = 1
                check_outside(storage, i, j) # 외부와 연결되어 있는지 확인

def fork(storage, req):
    row_len = len(storage)
    col_len = len(storage[0])
    
    # 바깥쪽 제외한 내부 컨테이너 출고 가능 여부 체크
    to_remove_position = []
    for i in range(1, row_len - 1):
        for j in range(1, col_len - 1):
            if (storage[i][j] == req and 
                (storage[i+1][j] == 0 or storage[i-1][j] == 0 or
                 storage[i][j+1] == 0 or storage[i][j-1] == 0)):
                to_remove_position.append([i, j])
    
    # 바깥 컨테이너 check
    for i in range(row_len - 1):
        if i == 0:
            for j in range(col_len):
                if storage[i][j] == req: # 첫번째 행 check
                    to_remove_position.append([i, j])
                if storage[row_len - 1][j] == req: # 마자막 행 check
                    to_remove_position.append([row_len - 1, j])
        else: # 중간 행 양끝 check
            if storage[i][0] == req:
                to_remove_position.append([i, 0])
            if storage[i][col_len - 1] == req:
                to_remove_position.append([i, col_len - 1])
                
    # 컨테이너 출고
    for row, col in to_remove_position:
        storage[row][col] = 0
        check_outside(storage, row, col) # 외부와 연결되어 있는지 확인
        
    
def solution(storage, requests):
    answer = 0
    storage = [list(row) for row in storage] # 2차원 배열로 변경
    # print(storage)
    
    for req in requests:
        if len(req) == 1:
            fork(storage, req)
        else:
            crane(storage, req[0])
        # print(storage)
    
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] != 0 and storage[i][j] != 1:
                answer += 1
    return answer