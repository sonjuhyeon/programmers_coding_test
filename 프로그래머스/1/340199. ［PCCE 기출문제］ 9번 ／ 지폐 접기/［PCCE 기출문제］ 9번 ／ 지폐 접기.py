def solution(wallet, bill):
    answer = 0
    while not (
        (wallet[0] >= bill[0] and wallet[1] >= bill[1]) or 
        (wallet[0] >= bill[1] and wallet[1] >= bill[0])
    ):  
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
        
    return answer