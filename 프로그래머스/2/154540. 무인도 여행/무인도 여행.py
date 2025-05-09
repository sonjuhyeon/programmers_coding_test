from collections import deque

def solution(maps):
    answer = []
    row_n = len(maps)
    col_n = len(maps[0])
    
    visited = set()
    for i in range(row_n):
        for j in range(col_n):
            if (i, j) in visited or maps[i][j] == 'X':
                continue
            else:
                dq = deque([(i, j)])
                days = 0
                dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
                
                while dq:
                    r, c = dq.popleft()
                    visited.add((r, c))
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if (
                            0 <= nr < row_n and 
                            0 <= nc < col_n and 
                            (nr, nc) not in visited and
                            maps[nr][nc] != 'X'
                        ):
                            dq.append([nr, nc])
                            visited.add((nr, nc))
                        else:
                            continue
                    days += int(maps[r][c])
                answer.append(days)
    answer.sort()
    return answer if answer else [-1]