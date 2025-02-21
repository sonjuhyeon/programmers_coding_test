from itertools import combinations

def solution(n, q, ans):
    answer = 0
    n_lst = [i for i in range(1, n+1)]
    m = len(ans)
    
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