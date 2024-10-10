from collections import defaultdict
from itertools import combinations

def add_info(info):
    # 모든 가능한 조건 조합을 저장할 딕셔너리 생성
    info_dict = defaultdict(list)
    for inf in info:
        condition = inf.split()
        score = int(condition[-1])
        condition = condition[:-1]
        # 모든 조합에 대해 값을 저장
        for r in range(5):
            for comb in combinations(range(4), r):
                temp_condition = condition[:]
                for idx in comb:
                    temp_condition[idx] = '-'
                info_dict[tuple(temp_condition)].append(score)
    
    # 각 리스트를 정렬하여 이진 탐색을 사용할 수 있도록 준비
    for key in info_dict:
        info_dict[key].sort()
    
    return info_dict

def count_scores(scores, query_score):
    # 이진 탐색을 통해 query_score 이상의 값을 빠르게 카운트
    left, right = 0, len(scores)
    while left < right:
        mid = (left + right) // 2
        if scores[mid] >= query_score:
            right = mid
        else:
            left = mid + 1
    return len(scores) - left

def solution(info, query):
    info_dict = add_info(info)
    answer = []
    
    for q in query:
        q_split = q.split(' and ')
        food_score = q_split[-1].split()
        q_split[-1] = food_score[0]
        query_key = tuple(q_split)
        query_score = int(food_score[1])
        
        if query_key in info_dict:
            scores = info_dict[query_key]
            answer.append(count_scores(scores, query_score))
        else:
            answer.append(0)
    
    return answer
