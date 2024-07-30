def check_only_blank(s):
    for i in range(len(s)):
        if (s[i] != ' '):
            return (0)
    return (1)

def solution(babbling):
    answer = 0
    split_word = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        if (i != ''):
            string = i
            for j in split_word:
                spl_i = string.split(j)
                string = ' '.join(spl_i)
            if check_only_blank(string):
                answer += 1
    return answer