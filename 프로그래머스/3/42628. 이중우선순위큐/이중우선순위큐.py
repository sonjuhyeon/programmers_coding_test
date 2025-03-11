import heapq

def solution(operations):
    min_heap = []
    answer = []
    
    for op in operations:
        command, value = op.split(' ')
        value = int(value)
        if command == 'I':
            heapq.heappush(min_heap, value)
        else:
            if min_heap:
                if value == -1:
                    heapq.heappop(min_heap)
                else:
                    # 최대 힙 구현 (음수 변환)
                    max_heap = [-x for x in min_heap]  # 모든 값을 음수로 변환하여 최대 힙 생성
                    heapq.heapify(max_heap)
                    heapq.heappop(max_heap)  # 최대값 삭제
                    min_heap = [-x for x in max_heap]  # 다시 최소 힙 형태로 변환
                    heapq.heapify(min_heap)
        
    if not min_heap:
        return [0, 0]

    return [max(min_heap), min(min_heap)]