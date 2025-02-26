def solution(people, limit):
    answer = 0
    people.sort()
    
    min_idx = 0
    max_idx = len(people) - 1
    people_count = len(people)
    
    while people_count > 0:
        if people_count == 1:
            answer += 1
            break
        if people[min_idx] + people[max_idx] <= limit:
            min_idx += 1
            people_count -= 1
        max_idx -= 1
        people_count -= 1
        answer += 1
    return answer