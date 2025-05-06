def solution(sticker):
    size = len(sticker)
    if size == 1:
        return sticker[0]
    elif size == 2:
        return max(sticker[0], sticker[1])
    
    # 인덱스 0을 고르고 시작하였을 경우
    dp1 = [0 for _ in range(size - 1)]
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    
    for i in range(2, len(dp1)):
        dp1[i] = max(dp1[i - 1], dp1[i - 2]  + sticker[i])
    
    # 인덱스 1을 고르고 시작하였을 경우
    dp2 = [0 for _ in range(size)]
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, size):
        dp2[i] = max(dp2[i - 1], dp2[i - 2]  + sticker[i])
    
    return max(dp1[-1], dp2[-1])