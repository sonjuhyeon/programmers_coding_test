def dfs(v, visited, computers):
    """
    DFS를 사용하여 연결된 네트워크(그래프)를 탐색하는 함수.
    방문한 노드를 visited 집합에 추가하고, 연결된 노드를 재귀적으로 탐색.
    
    :param v: 현재 방문 중인 노드 (컴퓨터 번호)
    :param visited: 방문한 노드 집합
    :param computers: 네트워크 연결 정보를 담은 인접 행렬
    """
    visited.add(v)  # 현재 노드를 방문했다고 표시
    for i in range(len(computers)):  # 모든 노드(컴퓨터) 탐색
        if computers[v][i] == 1 and i not in visited:  # 연결된 노드이며 방문하지 않았다면
            dfs(i, visited, computers)  # DFS 재귀 호출


def solution(n, computers):
    """
    주어진 네트워크(인접 행렬)에서 네트워크 개수를 구하는 함수.

    :param n: 컴퓨터의 개수 (노드의 개수)
    :param computers: 네트워크 연결 정보를 담은 n x n 인접 행렬
    :return: 네트워크 개수 (연결된 그래프 개수)
    """
    visited = set()  # 방문한 노드를 저장하는 집합 (set)
    count = 0  # 네트워크 개수를 저장하는 변수

    for i in range(n):  # 모든 노드(컴퓨터)에 대해 확인
        if i not in visited:  # 방문하지 않은 노드라면
            dfs(i, visited, computers)  # DFS 실행 (연결된 네트워크 탐색)
            count += 1  # 탐색이 끝나면 네트워크 개수 증가

    return count  # 네트워크 개수 반환

