# 행렬의 시작점은 좌하단에서 (1, 1)로 시작
def solution(n, w, num):
    last_row = n // w + 1 # 마지막 행 위치
    target_row = num // w + 1 # 꺼내려는 상자의 행 위치
    
    if n % w == 0:
        last_row -= 1
    if num % w == 0:
        target_row -= 1
    
    
    # 마지막 상자의 column 위치 구하기
    if last_row % 2 == 1:
        last_col = n % w # 행의 개수가 홀수 일 때 오른쪽 방향
        if last_col == 0:
            last_col = w
    else:
        last_col = w - (n % w) + 1# 짝수 일 때 왼쪽 방향
        if last_col == w + 1:
            last_col = 1
    
    # 꺼내려는 상자의 column 위치
    if target_row % 2 == 1:
        target_col = num % w # 행의 개수가 홀수 일 때 오른쪽 방향
        if target_col == 0:
            target_col = w
    else:
        target_col = w - (num % w) + 1 # 짝수 일 때 왼쪽 방향
        if target_col == w + 1:
            target_col = 1
        
        
    # 마지막 행과 꺼내려는 행이 둘다 짝수 일 때
    if last_row % 2 == 0 and target_row % 2 == 0:
        answer = last_row - target_row
        if last_col <= target_col:
            answer += 1
    # 마지막 행과 꺼내려는 행이 둘다 홀수 일 때
    elif last_row % 2 == 1 and target_row % 2 == 1:
        answer = last_row - target_row
        if last_col >= target_col:
            answer += 1
    # 미자막 행은 홀수 꺼내려는 행은 짝수 일 때
    elif last_row % 2 == 1 and target_row % 2 == 0:
        answer = last_row - target_row
        if last_col >= target_col:
            answer += 1
    # 미자막 행은 짝수 꺼내려는 행은 홀수 일 때
    else:
        answer = last_row - target_row
        if last_col <= target_col:
            answer += 1
    print(f"last_box: {last_row}, {last_col}")
    print(f"target_box: {target_row}, {target_col}")
    return answer