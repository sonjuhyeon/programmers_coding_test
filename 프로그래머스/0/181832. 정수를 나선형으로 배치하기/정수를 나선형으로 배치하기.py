d = [[0, 1],[1, 0],[0, -1],[-1, 0]]

def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    dt = 0

    for i in range(1, n * n + 1):
        answer[x][y] = i
        xx, yy = x + d[dt][0], y + d[dt][1]
        if 0 <= xx < n and 0 <= yy < n:
            if answer[xx][yy] != 0:
                dt = (dt + 1) % 4
                x, y = x + d[dt][0], y + d[dt][1]
            else:
                x, y = xx, yy
        else:
            dt = (dt + 1) % 4
            x, y = x + d[dt][0], y + d[dt][1]


    return answer