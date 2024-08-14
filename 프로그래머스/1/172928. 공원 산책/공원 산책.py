def east_check(col, park, t):
    if col + t >= len(park):
        return (0)
    for i in range(col + 1, col + t + 1):
        if park[i] == "X":
            return (0)
    return (1)
        
def west_check(col, park, t):
    if col - t < 0:
        return (0)
    for i in range(col - 1, col - t - 1, -1):
        if park[i] == "X":
            return (0)
    return (1)

def south_check(row, park, t):
    if row + t >= len(park):
        return (0)
    for i in range(row + 1, row + t + 1):
        if park[i] == "X":
            return (0)
    return (1)

def north_check(row, park, t):
    if row - t < 0:
        return (0)
    for i in range(row - 1, row - t - 1, - 1):
        if park[i] == "X":
            return (0)
    return (1)

def solution(park, routes):
    answer = []
    park_col = []
    row_size = len(park)
    col_size = len(park[0])
    for i in range(col_size):
        col = []
        for j in range(row_size):
            col.append(park[j][i])
            if park[j][i] == "S":
                answer.append(j)
                answer.append(i)
        park_col.append(col)
        
    for task in routes:
        t = task.split(" ")
        t[1] = int(t[1])
        cur_row = answer[0]
        cur_col = answer[1]
        if (t[0] == "E"):
            if east_check(cur_col, park[cur_row], t[1]):
                answer[1] += t[1]
        elif (t[0] == "W"):
            if west_check(cur_col, park[cur_row], t[1]):
                answer[1] -= t[1]
        elif (t[0] == "S"):
            if south_check(cur_row, park_col[cur_col], t[1]):
                answer[0] += t[1]
        else:
            if north_check(cur_row, park_col[cur_col], t[1]):
                answer[0] -= t[1]
    return answer