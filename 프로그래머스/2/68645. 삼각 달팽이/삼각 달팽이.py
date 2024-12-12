import math

def create_down_steps(n):
    result = []
    first_element = 0
    second_element = 0
    
    for i in range(n):
        result.append([first_element, second_element])
        first_element += 2
        second_element += 1
    
    return result

def create_right_steps(n):
    result = []
    first_element = -1
    second_element = 1
    for i in range(n):
        result.append([first_element, second_element])
        first_element -= 1
        second_element += 1
    return result

def create_up_steps(n):
    result = []
    first_element = -2
    second_element = -1
    for i in range(n):
        result.append([first_element, second_element])
        first_element -= 1
        second_element -= 1
    return result

def insert_down(snail_arr, start_position, val_to_insert):
    row = start_position[0]
    col = start_position[1]
    for i in val_to_insert:
        snail_arr[row][col] = i
        row += 1
        
def insert_right(snail_arr, start_position, val_to_insert):
    row = start_position[0]
    col = start_position[1]
    for i in val_to_insert:
        snail_arr[row][col] = i
        col += 1
        
def insert_up(snail_arr, start_position, val_to_insert):
    row = start_position[0]
    col = start_position[1]
    for i in val_to_insert:
        snail_arr[row][col] = i
        row -= 1


def solution(n):
    snail_arr = []
    for i in range(1, n + 1):
        snail_arr.append([0] * i)

    down_steps = create_down_steps(math.ceil(n / 3))
    right_steps = create_right_steps(math.ceil(n / 3) if n % 3 == 2 else n // 3)
    up_steps = create_up_steps(n // 3)

    count = 1
    for i, v in enumerate(range(n, 0, -1)):
        lst = list(range(count, count + v))
        count += v
        if i % 3 == 0:
            insert_down(snail_arr, down_steps[i // 3], lst)
        elif i % 3 == 1:
            insert_right(snail_arr, right_steps[i // 3], lst)
        else:
            insert_up(snail_arr, up_steps[i // 3], lst)
            
    answer = [item for sublist in snail_arr for item in sublist]
    
    return answer