from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 1. 원형 구조를 일자 선형으로 바꾸기 위해 weak를 두 배로 확장
    weak_extended = weak + [w + n for w in weak]
    min_count = len(dist) + 1  # 최악의 경우보다 큰 값으로 초기화

    # 2. 친구 순열을 모두 시도
    for friends in permutations(dist):
        # 3. 모든 시작점에 대해 시뮬레이션
        for start in range(length):
            count = 1  # 친구 수
            # 현재 친구가 커버할 수 있는 마지막 위치
            position = weak_extended[start] + friends[count - 1]
            
            # 시작점부터 점검 가능한 위치까지 커버 가능한지 확인
            for idx in range(start + 1, start + length):
                if weak_extended[idx] > position:
                    count += 1  # 다음 친구 투입
                    if count > len(dist):  # 친구 부족
                        break
                    position = weak_extended[idx] + friends[count - 1]
                    
            min_count = min(min_count, count)
    
    return min_count if min_count <= len(dist) else -1
