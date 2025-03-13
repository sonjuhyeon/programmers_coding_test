def queen_ck(array, row, column):
    for i in range(column):
        if array[i] == row:
            return False
        if abs(array[i] - row) == abs(i - column):
            return False
    return True

def recursive(array, count, row, column, n):
    if column == n:
        count[0] += 1
        return

    for i in range(row, n):
        if queen_ck(array, i, column):
            array[column] = i
            recursive(array, count, 0, column + 1, n)
            if i + 1 < n:
                recursive(array, count, i + 1, column, n)
            return

def solution(n):
    count = [0]  # 리스트를 사용하여 참조 가능하게 설정
    array = [-1] * n  # 퀸의 위치를 저장하는 배열
    recursive(array, count, 0, 0, n)
    return count[0]