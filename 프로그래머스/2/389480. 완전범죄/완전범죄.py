from collections import deque

def solution(info, n, m):
    answer = 0
    info = deque(info)
    vestiges_lst = deque([])
    
    if info[0][0] < n:
        vestiges_lst.append([info[0][0], 0])
    if info[0][1] < m:
        vestiges_lst.append([0, info[0][1]])
    if not vestiges_lst:
        return -1
    
    info.popleft()
    
    while info:
        inf = info.popleft()
        new_vestiges_lst = set() # 중복 방지를 위한 set
        
        while vestiges_lst:
            a, b = vestiges_lst.popleft()
            if a + inf[0] < n:
                new_vestiges_lst.add((a + inf[0], b))
            if b + inf[1] < m:
                new_vestiges_lst.add((a, b + inf[1]))
                
        vestiges_lst.extend(new_vestiges_lst) # 새로운 흔적 리스트 큐에 추가
        
    a_vestiges = [row[0] for row in vestiges_lst]
    
    return min(a_vestiges) if a_vestiges else -1