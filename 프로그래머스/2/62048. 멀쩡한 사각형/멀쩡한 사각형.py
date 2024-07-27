def greatest_common_divisor(n, m):
    if m == 0:
        return n
    else:
        return greatest_common_divisor(m, n % m)
    
def solution(w,h):
    area = w * h
    gcd = greatest_common_divisor(w, h)
    scale = [w/gcd, h/gcd]
    cut_block = (scale[0] * scale[1]) - ((scale[0] - 1) * (scale[1]-1))
    
    answer = area - (cut_block * gcd)
    return answer