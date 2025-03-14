from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    dq = deque()
    dq.append((begin, 0))
    
    while dq:
        visited = [0] * len(words)
        word, answer = dq.popleft()
        if word == target:
            break
        for i in range(len(words)):
            for j in range(len(words[i])):
                if word[j] == words[i][j]:
                    visited[i] += 1
                    
        for k in range(len(visited)):
            if visited[k] == (len(target) - 1):
                dq.append((words[k], answer + 1))
                words[k] = str(answer)
    
    return answer