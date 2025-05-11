def solution(numbers, hand):
    # 키패드 위치를 딕셔너리로 정의
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    # 초기 위치
    left_pos = keypad['*']
    right_pos = keypad['#']
    answer = []

    # 거리 계산 함수
    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    for number in numbers:
        # 왼손으로 누르는 숫자
        if number in [1, 4, 7]:
            answer.append('L')
            left_pos = keypad[number]
        # 오른손으로 누르는 숫자
        elif number in [3, 6, 9]:
            answer.append('R')
            right_pos = keypad[number]
        # 중앙 숫자 (2, 5, 8, 0)
        else:
            left_dist = distance(left_pos, keypad[number])
            right_dist = distance(right_pos, keypad[number])

            # 가까운 손으로 누르기
            if left_dist < right_dist:
                answer.append('L')
                left_pos = keypad[number]
            elif right_dist < left_dist:
                answer.append('R')
                right_pos = keypad[number]
            else:
                # 거리가 같으면 주 손잡이 사용
                if hand == "right":
                    answer.append('R')
                    right_pos = keypad[number]
                else:
                    answer.append('L')
                    left_pos = keypad[number]

    return ''.join(answer)