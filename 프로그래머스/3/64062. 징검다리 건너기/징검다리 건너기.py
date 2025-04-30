def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        skip = 0
        can_cross = True
        
        for stone in stones:
            if stone < mid:
                skip += 1
                if skip >= k:
                    can_cross = False
                    break
            else:
                skip = 0
        
        if can_cross:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer