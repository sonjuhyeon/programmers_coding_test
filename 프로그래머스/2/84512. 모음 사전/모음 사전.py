from itertools import product

def solution(word):
    vowel_dict = []
    words = ['A','E','I','O','U']
    for i in range(1,6):
        for j in product(words, repeat=i):
            vowel_dict.append(''.join(j))
    
    vowel_dict.sort()
    answer = vowel_dict.index(word) + 1
    return answer
