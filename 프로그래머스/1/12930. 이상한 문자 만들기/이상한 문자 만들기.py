def solution(s):
    words = s.split(" ")
    for i in range(len(words)):
        word = list(words[i])
        for j, char in enumerate(word):
            if j % 2 == 0:
                word[j] = char.upper()
            else:
                word[j] = char.lower()
        words[i] = "".join(word)
    answer = " ".join(words)
    return answer