from itertools import permutations

def operator(symbol, n1, n2):
    if symbol == '*':
        return n1 * n2
    elif symbol == '-':
        return n1 - n2
    elif symbol == '+':
        return n1 + n2

def solution(expression):
    answer = []
    numbers = []
    symbols = []
    n_tmp = ''
    for char in expression:
        if char.isdigit():
            n_tmp += char
        else:
            symbols.append(char)
            numbers.append(int(n_tmp))
            n_tmp = ''
    numbers.append(int(n_tmp))
    
    perm_symbols = permutations(set(symbols), len(set(symbols)))
    for ps in perm_symbols:
        tmp_nb = numbers[:]
        tmp_sb = symbols[:]
        
        for symbol in ps:
            i = 0
            while i < len(tmp_sb):
                if symbol == tmp_sb[i]:
                    tmp_sb.pop(i)
                    tmp_nb[i] = operator(symbol, tmp_nb[i], tmp_nb.pop(i + 1))
                else:
                    i += 1
        answer.append(abs(tmp_nb[0]))
            
    return max(answer)