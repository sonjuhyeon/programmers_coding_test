from collections import deque

def solution(maps):
    answer = []
    row_n = len(maps)
    col_n = len(maps[0])
    
    visited = set()
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    
    for i in range(row_n):
        for j in range(col_n):
            # 방문했거나 'X'이면 건너뜀
            if (i, j) in visited or maps[i][j] == 'X':
                continue
            
            # BFS 탐색 시작
            dq = deque([(i, j)])
            visited.add((i, j))  # 큐에 넣을 때 방문 처리
            days = int(maps[i][j])  # 시작점의 값 누적
            
            while dq:
                r, c = dq.popleft()
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if (
                        0 <= nr < row_n and 
                        0 <= nc < col_n and 
                        (nr, nc) not in visited and
                        maps[nr][nc] != 'X'
                    ):
                        dq.append((nr, nc))
                        visited.add((nr, nc))
                        days += int(maps[nr][nc])
            
            answer.append(days)
    
    answer.sort()
    return answer if answer else [-1]
