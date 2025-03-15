def solution(n, lost, reserve):
    
    # 여벌 체육복을 가지고 있으면서 도난 당한 학생의 번호
    lost_reserve = [l for l in lost if l in reserve]
    
    # 중복 제거
    lost = [x for x in lost if x not in lost_reserve]
    reserve = [x for x in reserve if x not in lost_reserve]
    
    for student in sorted(reserve):
        if student - 1 in lost:
            lost.remove(student - 1)
        elif student + 1 in lost:
            lost.remove(student + 1)
    
    answer = n - len(lost)
    return answer