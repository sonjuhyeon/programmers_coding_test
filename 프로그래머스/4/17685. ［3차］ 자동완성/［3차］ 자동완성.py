def common_prefix_length(str1, str2):
    length = 0
    for c1, c2 in zip(str1, str2):
        if c1 == c2:
            length += 1
        else:
            break
    return length

def solution(words):
    words.sort()
    answer = 0
    len_words = len(words)
    
    prefix_len = common_prefix_length(words[0], words[1])
    answer += prefix_len if prefix_len == len(words[0]) else prefix_len + 1
    
    for i in range(1, len_words - 1):
        prefix_len_prev = common_prefix_length(words[i], words[i - 1])
        prefix_len_next = common_prefix_length(words[i], words[i + 1])
        max_prefix_len = max(prefix_len_prev, prefix_len_next)
        answer += max_prefix_len if max_prefix_len == len(words[i]) else max_prefix_len + 1
            
    prefix_len = common_prefix_length(words[-1], words[-2])
    answer += prefix_len if prefix_len == len(words[-1]) else prefix_len + 1
    
    return answer