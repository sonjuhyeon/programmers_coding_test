from collections import deque

def solution(board):
    N = len(board)
    cost = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    dq = deque()

    # 상하좌우: 방향 0,1,2,3
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for d in range(4):  # 시작점을 4방향 모두로 초기화
        cost[0][0][d] = 0
        dq.append((0, 0, 0, d))  # row, col, 현재까지 비용, 방향

    while dq:
        r, c, curr_cost, prev_d = dq.popleft()

        for d, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                # 방향 유지: 직선, 방향 변경: 코너 비용
                next_cost = curr_cost + (100 if d == prev_d else 600)
                if cost[nr][nc][d] > next_cost:
                    cost[nr][nc][d] = next_cost
                    dq.append((nr, nc, next_cost, d))
    return min(cost[N-1][N-1])  # 도착점까지 4방향 중 최소 비용