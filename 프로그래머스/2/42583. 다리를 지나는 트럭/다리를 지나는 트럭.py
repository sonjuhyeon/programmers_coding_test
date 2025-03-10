from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    current_weight = 0
    
    # 진입 시간과 트럭의 무게를 이차원 리스트로 저장 [[2, 7], [4, 10]] -> 2초에 7kg 트럭, 4초에 10kg 트럭 진입
    on_bridge = deque()
    
    while truck_weights:
        answer += 1
        
        # 다리에서 나갈 트럭 체크
        if on_bridge:
            t, w = on_bridge[0]
            if answer - t == bridge_length:
                on_bridge.popleft()
                current_weight -= w
        
        # 새로운 트럭 진입 가능 여부 체크
        if truck_weights[0] + current_weight <= weight:
            truck_w = truck_weights.popleft()
            on_bridge.append([answer, truck_w])
            current_weight += truck_w
            
    answer += bridge_length
    
        
    return answer