from collections import deque

def bfs(v, visited, computers):
    """
    BFS를 사용하여 연결된 네트워크를 탐색하는 함수.
    :param v: 시작 노드
    :param visited: 방문한 노드 집합
    :param computers: 네트워크 연결 정보를 담은 인접 행렬
    """
    queue = deque([v])  # 큐를 생성하면서 v를 초기 값으로 추가
    visited.add(v)  # 방문 처리

    while queue:  # 큐가 빌 때까지 반복
        target = queue.popleft()  # 큐에서 노드 하나 꺼내기
        for i in range(len(computers)):  # 모든 노드 탐색
            if computers[target][i] == 1 and i not in visited:  # 연결된 노드이면서 방문하지 않은 경우
                queue.append(i)  # 큐에 추가
                visited.add(i)  # 방문 처리

def solution(n, computers):
    """
    BFS를 활용하여 네트워크 개수를 구하는 함수.
    :param n: 컴퓨터의 개수 (노드의 개수)
    :param computers: 네트워크 연결 정보를 담은 n x n 인접 행렬
    :return: 네트워크 개수 (연결된 그래프 개수)
    """
    visited = set()  # 방문한 노드를 저장하는 집합 (탐색 속도 향상)
    answer = 0  # 네트워크 개수 저장

    for i in range(n):  # 모든 노드(컴퓨터)를 확인
        if i not in visited:  # 방문하지 않은 노드라면
            bfs(i, visited, computers)  # BFS 수행
            answer += 1  # 네트워크 개수 증가

    return answer  # 네트워크 개수 반환
