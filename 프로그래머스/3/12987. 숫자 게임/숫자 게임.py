def solution(A, B):
    score = 0
    A.sort()
    B.sort()
    a_weakest = 0
    
    for b in B:
        if b > A[a_weakest]:
            a_weakest += 1
            score += 1
    return score