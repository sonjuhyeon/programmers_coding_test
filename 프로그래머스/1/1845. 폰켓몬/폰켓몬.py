from collections import defaultdict

def solution(nums):
    answer = 0
    dic = defaultdict(int)
    
    for n in nums:
        dic[n] += 1
    
    half = len(nums) // 2
    number_of_pocketmon = len(dic)
    
    answer = min(half, number_of_pocketmon)
    return answer