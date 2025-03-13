def solution(sizes):
    wallet_size = [0, 0]
    
    for width, height in sizes:
        wallet_size[0] = max(width, height, wallet_size[0])
        wallet_size[1] = max(min(width, height), wallet_size[1])
    
    answer = wallet_size[0] * wallet_size[1]
    return answer