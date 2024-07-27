import math

def greatest_common_divisor(n, m):
    if m == 0:
        return n
    else:
        return greatest_common_divisor(m, n % m)
    
def solution(w,h):
    answer = 0
    area = w * h
    gcd = greatest_common_divisor(w, h)
    if (w > h):
        w, h = h, w
    scale = [w//gcd, h//gcd]
    ratio_lst = []
    cut_block = 0
    for i in range(1, scale[0] + 1):
        ratio = scale[1] * i / scale[0]
        ratio_lst.append(ratio)
    
    for i in range(len(ratio_lst)):
        if i == 0:
            cut_block += (math.ceil(ratio_lst[i]))
        else:
            cut_block += (math.ceil(ratio_lst[i]) - math.floor(ratio_lst[i - 1]))
    answer = area - (gcd * cut_block) 
    return answer