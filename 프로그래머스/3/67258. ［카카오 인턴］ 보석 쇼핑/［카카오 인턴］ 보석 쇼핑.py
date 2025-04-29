from collections import defaultdict

def solution(gems):
    gem_types = len(set(gems))
    gem_counter = defaultdict(int)
    answer = [0, len(gems) - 1]  # 최악의 경우 (전체)
    
    left = 0
    for right in range(len(gems)):
        gem_counter[gems[right]] += 1

        while len(gem_counter) == gem_types:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            
            gem_counter[gems[left]] -= 1
            if gem_counter[gems[left]] == 0:
                del gem_counter[gems[left]]
            left += 1
    
    return [answer[0] + 1, answer[1] + 1]