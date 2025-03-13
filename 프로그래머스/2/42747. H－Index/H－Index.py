def solution(citations):
    answer = 0
    n_theses = len(citations)
    citations = sorted(citations)
    print(citations)
    
    for i in range(n_theses):
        if citations[i] >= n_theses - i:
            answer = n_theses - i
            break
    return answer