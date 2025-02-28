def base26_to_decimal(string):
    result = 0
    nth = 0 # 자리수 (26^0 자리)
    for i in range(len(string) - 1, -1 , -1):
        result += 26 ** nth * (ord(string[i]) - ord('a') + 1)
        nth += 1
    return result

def decimal_to_base26(n):
    result = []
    
    while n > 0:
        n -= 1
        result.insert(0, chr(ord('a') + (n % 26)))
        n //= 26
    return ''.join(result)
        
def solution(n, bans):
    answer = ''

    bans = [base26_to_decimal(ban) for ban in bans]
    bans.sort()

    for ban in bans:
        if ban <= n:
            n += 1
        else:
            break

    return decimal_to_base26(n)
