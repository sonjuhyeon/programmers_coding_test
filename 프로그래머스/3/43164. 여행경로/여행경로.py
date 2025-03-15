from collections import defaultdict
import heapq

def solution(tickets):
    graph = defaultdict(list)

    # 그래프 구성: 도착지를 min-heap에 삽입
    for start, end in tickets:
        heapq.heappush(graph[start], end)

    path = []
    
    def dfs(airport):
        while graph[airport]:
            next_airport = heapq.heappop(graph[airport])
            dfs(next_airport)
        path.insert(0, airport)

    dfs("ICN")  # 항상 ICN에서 시작
    return path