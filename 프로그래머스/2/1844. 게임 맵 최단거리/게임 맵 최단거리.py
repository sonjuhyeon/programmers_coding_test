from collections import deque

# BFS 함수
def bfs(maps):
    queue = deque([(1, 1)])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]

            if maps[nr][nc] == 1:
                # 이동 거리 (이전 거리 + 1)
                maps[nr][nc] = maps[row][col] + 1
                queue.append((nr, nc))

def solution(maps):
    row_len, col_len = len(maps), len(maps[0])
    maps = [[0] + row + [0] for row in maps]
    maps.insert(0, [0] * (col_len + 2))
    maps.append([0] * (col_len + 2))
    
    bfs(maps)
    
    if maps[row_len][col_len] == 1:
        return -1
    else:
        return maps[row_len][col_len]