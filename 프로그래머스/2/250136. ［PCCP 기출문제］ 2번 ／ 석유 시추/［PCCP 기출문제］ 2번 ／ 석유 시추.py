def find_coordinate(oil, x_size, y_size):
    res = []
    r = oil[0]
    c = oil[1]
        
    if (r == 0):
        res.append([r + 1, c])
    elif (r == y_size - 1):
        res.append([r - 1, c])
    else:
        res.append([r - 1, c])
        res.append([r + 1, c])
    
    if (c == 0):
        res.append([r, c + 1])
    elif (c == x_size - 1):
        res.append([r, c - 1])
    else:
        res.append([r, c - 1])
        res.append([r, c + 1])
    return (res)

def bfs(land, row, col, x, y, visited, answer_lst):
    queue = []
    res = [0] * x
    queue.append([row, col])
    visited[row][col] = True
    visited_col = []
    visited_col.append(col)
    number_of_group_oil = 1
    
    
    while (queue != []):
        near_queue = find_coordinate(queue[0], x, y)
        queue.remove(queue[0])
        for check in near_queue:
            cr = check[0]
            cc = check[1]
            if (visited[cr][cc] == False) and (land[cr][cc] == 1):
                queue.append([cr, cc])
                visited[cr][cc] = True
                number_of_group_oil += 1
                if not(cc in visited_col):
                    visited_col.append(cc)
                
    for i in visited_col:
        answer_lst[i] += number_of_group_oil

def solution(land):
    x_size = len(land[0])
    y_size = len(land)
    visited = []
    answer_lst = [0] * x_size

    for i in range(y_size):
        visited.append([False] * x_size)
    # visited = [[False] * x_size for _ in range(y_size)]
    
    for col in range(x_size):
        for row in range(y_size):
            if (land[row][col] == 1) and (visited[row][col] == False):
                bfs(land, row , col, x_size, y_size, visited, answer_lst)
    answer = max(answer_lst)

    return answer