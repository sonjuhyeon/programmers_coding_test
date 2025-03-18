def solution(n, results):
    # 1. 그래프 초기화 (승패 관계 저장)
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    
    # 승리(1) / 패배(-1) 기록
    for winner, loser in results:
        graph[winner][loser] = 1   # 이겼으면 1
        graph[loser][winner] = -1  # 졌으면 -1
        
    # 2. 플로이드-와샬 알고리즘 적용 (간접 승패 관계 전파)
    for k in range(1, n + 1):        # 중간 선수
        for i in range(1, n + 1):    # 출발 선수
            for j in range(1, n + 1):# 도착 선수
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1  # i가 k를 이기고, k가 j를 이기면 i는 j를 이김
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1 # i가 k에게 지고, k가 j에게 지면 i는 j에게 짐

    # 3. 정확한 순위를 알 수 있는 선수 수 계산
    answer = 0
    for i in range(1, n + 1):
        count = graph[i].count(1) + graph[i].count(-1) # 승리 또는 패배가 기록된 수
        if count == n - 1:  # 모든 상대와 경기 결과가 결정된 경우
            answer += 1

    return answer
