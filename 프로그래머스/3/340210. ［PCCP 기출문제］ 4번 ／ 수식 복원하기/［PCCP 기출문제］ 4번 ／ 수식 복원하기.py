def get_min_base(expressions):
    min_base = []
    for exp in expressions:
        exp = list(exp)
        min_base.extend([e for e in exp if e.isdigit()])
    return int(max(min_base)) + 1

def check_base(n1, n2, ans, base):
    n1 = int(str(n1), base)
    n2 = int(str(n2), base)
    ans = int(str(ans), base)
    if n1 + n2 == ans or n1 - n2 == ans:
        return 1
    return 0

def get_possible_base(n1, n2, ans, is_possible_base):
    res = []
    for base in is_possible_base:
        if check_base(n1, n2, ans, base):
            res.append(base)
    return res

def to_base_n(num, base):
    digits = "0123456789"
    if num == 0:
        return "0"
    
    res = ""
    while num > 0:
        res = digits[num % base] + res
        num //= base
    return res


def solution(expressions):
    answer = []
    min_base = get_min_base(expressions)
    is_possible_base = list(range(min_base, 10))
    x_exp = []
    
    for exp in expressions:
        e, ans = exp.split(' = ')
        if '-' in e:
            num1, num2 = e.split(' - ')
        else:
            num1, num2 = e.split(' + ')
        if ans == 'X':
            x_exp.append(exp)
        else:
            is_possible_base = get_possible_base(num1, num2, ans, is_possible_base)
    
    for exp in x_exp:
        ans_lst = set()
        for base in is_possible_base:
            e, ans = exp.split(' = ')
            if '-' in e:
                num1, num2 = e.split(' - ')
                op = '-'
            else:
                num1, num2 = e.split(' + ')
                op = '+'
            num1 = int(num1, base)
            num2 = int(num2, base)
            if op == '+':
                result = num1 + num2
            else:
                result = num1 - num2
            
            result = to_base_n(result, base)
            ans_lst.add(result)
        if len(ans_lst) != 1:
            answer.append(exp[:-1] + '?')
        else:
            answer.append(exp[:-1] + ans_lst.pop())
    return answer