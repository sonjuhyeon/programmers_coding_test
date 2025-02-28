def get_shape(node, graph_out):
    visited = set()
    
    while node not in visited:
        visited.add(node)
        
        if node not in graph_out:
            return "stick"  # 나가는 간선이 없는 노드
        elif len(graph_out[node]) == 2:
            return "eight"  # 나가는 간선이 2개인 경우
        
        node = graph_out[node][0]  # 다음 노드 이동
    
    return "donut"  # 사이클이 발생하면 donut
        

def solution(edges):
    visited = set()
    shapes = {"stick": 0, "donut": 0, "eight": 0}
    graph_out = {}
    graph_in = {}
    
    # graph_out 예제: {2: [3, 1], 4: [3], 1: [1]}
    # - 각 키(출발 노드)는 특정 노드로 향하는 간선을 가짐.
    # - 값(리스트)은 해당 키에서 출발하는 노드들의 목록을 나타냄.

    # graph_in 예제: {3: 2, 1: 2}
    # - 각 키(도착 노드)는 해당 노드로 들어오는 간선의 개수를 나타냄.

    for i, j in edges:
        if i not in graph_out:
            graph_out[i] = [j]
        else:
            graph_out[i].append(j)
        if j not in graph_in:
            graph_in[j] = 1
        else:
            graph_in[j] += 1
    
    # out이 2개 이상, in이 0개인 노드가 root
    for out in graph_out:
        if (out not in graph_in) and len(graph_out[out]) >= 2:
            root = out
            break
            
    # root와 연결된 각 그래프 모양 확인
    for start_node in graph_out[root]:
        shapes[get_shape(start_node, graph_out)] += 1

    return [root, shapes["donut"], shapes["stick"], shapes["eight"]]