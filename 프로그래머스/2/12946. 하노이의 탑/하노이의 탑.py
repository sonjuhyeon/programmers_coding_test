def hanoi(start, target, temp, n):
        if n == 1:
            return [[start, target]]
        return hanoi(start, temp, target, n - 1) + [[start, target]] + hanoi(temp, target, start, n - 1)

def solution(n):
    return hanoi(1, 3, 2, n)