def solution(data, col, row_begin, row_end):
    hash_val = []
    data.sort(reverse = True)
    data.sort(key = lambda x: x[col-1])
    
    hash_val = []
    for idx, row in enumerate(data[row_begin - 1:row_end], start=row_begin):
        mod_sum = sum(val % idx for val in row)
        hash_val.append(mod_sum)

    # XOR 계산
    answer = hash_val[0]
    for v in hash_val[1:]:
        answer ^= v
    
    return answer