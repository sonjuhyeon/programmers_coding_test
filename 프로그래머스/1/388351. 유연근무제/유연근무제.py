def solution(schedules, timelogs, startday):
    answer = 0
    
    # 주말 제외
    for tl in timelogs:
        tl.pop(7 - startday)
        tl.pop(6 - startday)
        
    # schedules 단위를 분으로 변환
    for i in range(len(schedules)):
        schedules[i] = (schedules[i] % 100) + ((schedules[i] // 100) * 60)
        
    
    for i in range(len(timelogs)):
        for tl in timelogs[i]:
            tl = (tl % 100) + (tl // 100 * 60)
            if tl > schedules[i] + 10:
                break
        else:
            answer += 1

    return answer