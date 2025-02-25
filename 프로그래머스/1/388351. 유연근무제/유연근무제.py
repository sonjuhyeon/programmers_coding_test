def solution(schedules, timelogs, startday):
    answer = 0
    
    # 주말 제외
    for tl in timelogs:
        tl.pop(7 - startday)
        tl.pop(6 - startday)
        
    # schedules 단위를 분으로 변환
    schedules = [(s % 100) + ((s // 100) * 60) for s in schedules]
    
    for i in range(len(timelogs)):
        # timelogs 단위를 분으로 변환
        timelogs[i] = [(timelog % 100) + ((timelog // 100) * 60) for timelog in timelogs[i]]
        for tl in timelogs[i]:
            if tl > schedules[i] + 10:
                break
        else:
            answer += 1

    return answer