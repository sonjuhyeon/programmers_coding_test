from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    answer = [-1] * (n + 1) # 방문 여부 및 1번 노드로부터 떨어진 거리 (-1이면 미방문)
    answer[1] = 0 # 시작 노드 거리는 0
    dq = deque([1]) # 시작 노드는 1
    
    while dq:
        node = dq.popleft()
        for neighbor in graph[node]:
            if answer[neighbor] == -1:
                answer[neighbor] = answer[node] + 1
                dq.append(neighbor)
    
    return answer.count(max(answer))