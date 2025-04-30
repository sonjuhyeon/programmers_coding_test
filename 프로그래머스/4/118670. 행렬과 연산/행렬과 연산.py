from collections import deque

def solution(rc, operations):
    row_n, col_n = len(rc), len(rc[0])

    # 3분할 구조
    left_col = deque()
    rows = deque()
    right_col = deque()

    for row in rc:
        left_col.append(row[0])
        rows.append(deque(row[1:-1]))
        right_col.append(row[-1])

    for op in operations:
        if op == "ShiftRow":
            # 세 덱 모두 rotate
            left_col.rotate(1)
            rows.rotate(1)
            right_col.rotate(1)
        elif op == "Rotate":
            # 위쪽 좌 -> 가운데로
            rows[0].appendleft(left_col.popleft())
            # 오른쪽 위로 이동
            right_col.appendleft(rows[0].pop())
            # 아래쪽 우 -> 가운데로
            rows[-1].append(right_col.pop())
            # 왼쪽 아래로 이동
            left_col.append(rows[-1].popleft())

    # 결과 복원
    answer = []
    for l, mid, r in zip(left_col, rows, right_col):
        answer.append([l] + list(mid) + [r])
    return answer
