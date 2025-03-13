from itertools import permutations

def solution(k, dungeons):
    enter_count = [0]
    perms = permutations(dungeons, len(dungeons))
    
    for perm in perms:
        count = 0
        current_k = k
        for necessary_k, used_k in perm:
            if current_k >= necessary_k:
                current_k -= used_k
                count += 1
        enter_count.append(count)
    answer = max(enter_count)
    return answer