def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, a, b):
    a_root = find(parent, a)
    b_root = find(parent, b)
    if a_root == b_root:
        return False  # 사이클 발생
    parent[b_root] = a_root
    return True

def solution(n, costs):
    answer = 0
    costs = sorted(costs, key = lambda x : x[2]) # cost 기준 정렬
    parent = [i for i in range(n)]

    for a, b, cost in costs:
        if union(parent, a, b):
            answer += cost

    return answer