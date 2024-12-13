import math

# down, right, up 방향으로 값을 삽입하는 함수
def insert(snail_arr, start_position, val_to_insert, direction):
    row, col = start_position
    for i in val_to_insert:
        snail_arr[row][col] = i
        if direction == 'down':
            row += 1
        elif direction == 'right':
            col += 1
        elif direction == 'up':
            row -= 1

# down, right, up 방향에 대한 step을 생성하는 함수
def create_steps(direction, n):
    result = []
    if direction == 'down':
        first_element, second_element = 0, 0
        for _ in range(n):
            result.append([first_element, second_element])
            first_element += 2
            second_element += 1
    elif direction == 'right':
        first_element, second_element = -1, 1
        for _ in range(n):
            result.append([first_element, second_element])
            first_element -= 1
            second_element += 1
    elif direction == 'up':
        first_element, second_element = -2, -1
        for _ in range(n):
            result.append([first_element, second_element])
            first_element -= 1
            second_element -= 1
    return result

def solution(n):
    # 나선형 배열을 만들기 위한 2D 배열 초기화
    snail_arr = [[0] * (i + 1) for i in range(n)]

    # 방향별 step을 생성
    down_steps = create_steps('down', math.ceil(n / 3))
    right_steps = create_steps('right', math.ceil(n / 3) if n % 3 == 2 else n // 3)
    up_steps = create_steps('up', n // 3)

    count = 1
    steps = [down_steps, right_steps, up_steps]
    direction = 0  # 0: down, 1: right, 2: up
    
    # 나선형으로 숫자 배치
    for i, v in enumerate(range(n, 0, -1)):
        lst = list(range(count, count + v))
        count += v
        insert(snail_arr, steps[direction][i // 3], lst, ['down', 'right', 'up'][direction])
        direction = (direction + 1) % 3  # 방향 전환 (down -> right -> up)

    # 2D 리스트를 1D 리스트로 변환
    return [item for sublist in snail_arr for item in sublist]
