def find_point_of_inter(l1, l2):

    x1, y1, c1 = l1
    x2, y2, c2 = l2

    # 행렬식 계산 (교차 여부 판단)
    determinant = (x1 * y2) - (y1 * x2)

    if determinant == 0:
        return None # 평행하거나 일치하는 직선

    x = (y1 * c2 - c1 * y2) / determinant
    y = (c1 * x2 - x1 * c2) / determinant

    if not x.is_integer() or not y.is_integer():
        return None

    return (int(x), int(y))


def display_points(points):
    xs, ys = zip(*points)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    grid = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'

    return [''.join(row) for row in grid]


def solution(line):
    intersection_points = set()

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            point = find_point_of_inter(line[i], line[j])
            if point:
                intersection_points.add(point)
                
    # print(intersection_points)
    return display_points(intersection_points)
