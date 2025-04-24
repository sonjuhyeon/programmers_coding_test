import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    # 최대 힙으로 만들기 (음수 사용)
    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        max_work = heapq.heappop(works)
        heapq.heappush(works, max_work + 1)  # +1, 즉 -1 감소
    
    answer = sum([w ** 2 for w in works])
    return answer
