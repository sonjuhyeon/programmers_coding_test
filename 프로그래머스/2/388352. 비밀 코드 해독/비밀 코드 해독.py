from itertools import combinations

def solution(n, q, ans):
    answer = 0
    n_lst = [i for i in range(1, n+1)]
    m = len(ans)
    
    to_remove_index = []
    # 못 맞춘 케이스의 index 찾기
    for i in range(len(ans)):
        if ans[i] == 0:
            to_remove_index.append(i)
    
    # 하나도 못 맞춘 인덱스의 값 제거
    for i in to_remove_index:
        for j in q[i]:
            try: lst.remove(j)
            except: pass
    
    # 가능한 모든 조합의 리스트
    comb_lst = list(combinations(n_lst, 5))
    
    for c in comb_lst:
        for i in range(m):
            cnt = 0
            for j in q[i]:
                if j in c:
                    cnt += 1
            if cnt != ans[i]:
                break
        else: # break가 실행되지 않았을 경우 모든 조건 충족
            answer += 1
            
    return answer