def solution(s, skip, index):
    answer = ''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for sk in skip:
        alphabet.remove(sk)
    
    answer = ''
    len_alpha = len(alphabet)
    for char in s:
        idx = alphabet.index(char)
        idx = (idx + index) % len_alpha
        answer += alphabet[idx]
    return answer