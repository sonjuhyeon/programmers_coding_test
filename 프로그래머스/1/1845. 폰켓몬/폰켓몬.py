from collections import defaultdict

def solution(nums):
    answer = 0
    dic = defaultdict(int)
    
    for n in nums:
        dic[n] += 1
    
    half = len(nums) // 2
    number_of_pocketmon = len(dic)
    
    
    if half > number_of_pocketmon:
        answer = number_of_pocketmon
    else:
        answer = half
    return answer