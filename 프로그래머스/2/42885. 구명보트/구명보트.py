def solution(people, limit):
    answer = 0
    people.sort()
    l = 0
    r = len(people) - 1
    while l <= r:
        if r == l:
            answer += 1
            break
        else:
            if (people[l] + people[r] <= limit):
                l += 1
            r -= 1
            answer += 1
    return answer