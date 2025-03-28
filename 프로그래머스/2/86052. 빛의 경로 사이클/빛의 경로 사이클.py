def get_next_position(grid, cur_pos, cur_dir):
    row_len = len(grid)
    col_len = len(grid[0])
    row = cur_pos[0] # 현재 row 위치
    col = cur_pos[1] # 현재 col 위치
    
    if cur_dir == 'R':
        col = (col + 1) % col_len
    elif cur_dir == 'L':
        col = (col - 1) % col_len
    elif cur_dir == 'U':
        row = (row - 1) % row_len
    elif cur_dir == 'D':
        row = (row + 1) % row_len

    return [row, col]

def get_next_direction(grid, cur_pos, cur_dir):
    node = grid[cur_pos[0]][cur_pos[1]]
    
    if node == 'S':
        return cur_dir

    direction_map = {
        'R': {
            'R': 'D',
            'L': 'U',
            'U': 'R',
            'D': 'L'
        },
        'L': {
            'R': 'U',
            'L': 'D',
            'U': 'L',
            'D': 'R'
        }
    }
    return direction_map[node][cur_dir]
        
def solution(grid):
    grid = [list(gr) for gr in grid]
    row_len = len(grid)
    col_len = len(grid[0])

    # 방문 배열: visited[row][col][dir_index]
    visited = [[[False] * 4 for _ in range(col_len)] for _ in range(row_len)]
    
    directions = ['R', 'D', 'L', 'U']
    dir_idx = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
    
    answer = []

    for r in range(row_len):
        for c in range(col_len):
            for d in directions:
                if not visited[r][c][dir_idx[d]]:
                    cur_pos = [r, c]
                    cur_dir = d
                    path_len = 0
                    
                    # 사이클 추적
                    while not visited[cur_pos[0]][cur_pos[1]][dir_idx[cur_dir]]:
                        visited[cur_pos[0]][cur_pos[1]][dir_idx[cur_dir]] = True
                        cur_pos = get_next_position(grid, cur_pos, cur_dir)
                        cur_dir = get_next_direction(grid, cur_pos, cur_dir)
                        path_len += 1

                    answer.append(path_len)

    return sorted(answer)
