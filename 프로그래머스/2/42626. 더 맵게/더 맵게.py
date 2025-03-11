import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    min_scoville = heapq.heappop(scoville)
    
    while min_scoville < K:
        if scoville:
            min_scoville_2nd = heapq.heappop(scoville)
        else:
            answer = -1
            break
        new_scoville = min_scoville + (min_scoville_2nd * 2)
        heapq.heappush(scoville, new_scoville)
        min_scoville = heapq.heappop(scoville)
        answer += 1
    
    return answer