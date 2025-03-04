def calc(numbers1, numbers2):
    res = set()
    for n1 in numbers1:
        for n2 in numbers2:
            res.add(n1 + n2)
            res.add(n1 - n2)
            res.add(n1 * n2)
            if n2 != 0:
                res.add(n1 // n2)
    return res

def solution(N, number):
    answer = -1
    result = {}
    result[1] = {N}
    
    if N == number:
        return 1
    
    for i in range(2, 9):
        tmp = {int(str(N) * i)}
        j = 1
        while j < i:
            tmp.update(calc(result[j], result[i - j]))
            j += 1
            
        if number in tmp:
            answer = i
            break
        result[i] = tmp
    return answer