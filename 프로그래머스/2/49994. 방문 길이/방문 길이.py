def next_location(x, y, d):
    if d == "U":
        next_x, next_y = x, y + 1
    elif d == "D":
        next_x, next_y = x, y - 1
    elif d == "R":
        next_x, next_y = x + 1, y
    else:
        next_x, next_y = x - 1, y
    
    if ((-5 <= next_x <= 5) and (-5 <= next_y <= 5)):
        return next_x, next_y
    else:
        return x, y

def solution(dirs):
    x, y = 0, 0
    answer = set()
    for d in dirs:
        next_x, next_y = next_location(x, y, d)
        if ((x == next_x) and (y == next_y)):
            continue
        answer.add((x, y, next_x, next_y))
        answer.add((next_x, next_y, x, y))
        x, y = next_x, next_y
    ret = len(answer) / 2
    return ret