####################################################
####################################################
#                    UNION-FIND                    #
####################################################
####################################################
def get_parent(v, arr):
    if arr[v] == v:
        return v
    else:
        return get_parent(arr[v],arr)

def union_parent(a,b, arr):
    a = get_parent(a, arr)
    b = get_parent(b, arr)
    if a<b:
        arr[b] = arr[a]
    else:
        arr[a] = arr[b]

def find_parent(a,b, arr):
    a = get_parent(a,arr)
    b = get_parent(b,arr)
    if a==b:
        return 1
    else:
        return 0


def solution(n, computers):
    answer = 1
    arr = []
    for i in range(n):
        arr.append(i)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif computers[i][j] == 1:
                union_parent(i,j,arr)

    ans = set()
    for i in range(n):
        ans.add(get_parent(i,arr))
    return len(ans)




#########################################################
#########################################################
#                         DFS                           #
#########################################################
#########################################################
def solution(n, computers):
    answer = 0
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                arr[i].append(j)
                arr[j].append(i)
    visited = []
    def dfs(v,visited,arr):
        if v not in visited:
            visited.append(v)
        for i in arr[v]:
            if i not in visited:
                visited = dfs(i,visited,arr)
        return visited
    count = 0
    for i in range(n):
        if i not in visited:
            visited = dfs(i,visited,arr)
            count+=1

    return count



#########################################################
#########################################################
#                         BFS                           #
#########################################################
#########################################################
from collections import deque
def solution(n, computers):
    answer = 0
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                arr[i].append(j)
                arr[j].append(i)

    def bfs(v, visited, arr):
        queue = deque()
        if v not in visited:
            visited.append(v)
            queue.append(v)
        while queue:
            target = queue.popleft()
            for i in arr[target]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return visited
    visited = []
    for i in range(n):
        if i not in visited:
            visited = bfs(i, visited, arr)
            answer+=1
    return answer