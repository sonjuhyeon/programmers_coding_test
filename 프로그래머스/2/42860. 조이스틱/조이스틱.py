def solution(name):
    answer = 0
    n = len(name)
    
    # 알파벳 변경 횟수 계산
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 커서 이동 최소값 찾기
    min_move = n - 1  # 기본적으로 오른쪽으로 쭉 가는 경우
    
    for i in range(n):
        next_idx = i + 1
        # 연속된 'A'의 가장 마지막 위치 찾기
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        # 현재 위치(i)에서 되돌아가는 경우 고려
        min_move = min(min_move, 2 * i + (n - next_idx), i + 2 * (n - next_idx))
    
    answer += min_move
    return answer
