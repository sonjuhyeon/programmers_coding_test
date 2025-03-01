def solution(lottos, win_nums):
    zero_cnt = 0
    match_cnt = 0
    
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
            continue
        if lotto in win_nums:
            match_cnt += 1
            
    highiest_rank =  7 - (match_cnt + zero_cnt)
    if highiest_rank == 7:
        highiest_rank = 6
    
    lowest_rank = 7 - match_cnt
    if lowest_rank == 7:
        lowest_rank = 6
        
    return [highiest_rank, lowest_rank]