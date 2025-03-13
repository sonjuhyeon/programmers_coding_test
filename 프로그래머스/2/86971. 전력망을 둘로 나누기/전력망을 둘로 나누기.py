from collections import defaultdict, deque

def bfs(w1, w2, graph):
    visited = [w1]
    dq = deque()
    dq.append(w2)
    
    while dq:
        node = dq.popleft()
        visited.append(node)
        for n in graph[node]:
            if n not in visited:
                dq.append(n)
    
    return len(visited) - 1
    

def solution(n, wires):
    answer = []
    graph = defaultdict(list)
    for w1, w2 in wires:
        graph[w1].append(w2)
        graph[w2].append(w1)
    
    for w1, w2 in wires:
        split_wires1 = bfs(w1, w2, graph)
        split_wires2 = n - split_wires1
        answer.append(abs(split_wires1 - split_wires2))
    
    return min(answer)