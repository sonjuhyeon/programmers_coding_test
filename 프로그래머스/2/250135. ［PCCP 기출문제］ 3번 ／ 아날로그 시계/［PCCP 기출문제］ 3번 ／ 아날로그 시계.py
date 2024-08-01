import math as m

def get_second(h, m, s):
    res = (h * 60 * 60) + (m * 60) + s
    return (res)

def get_count(sec):
    res = 1 # 0시 0분 0초에 알람
    
    # 시침과 만나 알람이 울리는 횟수
    # 초침은 시침과 1분에 한번씩 만남 (예외: 정오(11시 59분에서 12시)를 넘어갈때) 따라서 12시간을 기준으로 계산
    hour = (sec * (12 * 60 - 1)) / (12 * 60 * 60)
    
    # 분침과 만나 알람이 울리는 횟수
    # 초침은 분침과 1분에 한반씩 만남 (예외: 정각(x시 59분에서 x시)을 넘어갈 때) 따라서 1시간을 기준으로 계산
    minute = (sec * (60 - 1)) / (60 * 60)
    
    res += m.floor(hour) + m.floor(minute)
    
    # 12시간이 넘어가면 정오를 넘어간것임으로 -1
    if (sec >= 12 * 60 * 60):
        res -= 1
    
    print(hour, minute, int(hour), int(minute), res)
    return (res)

def get_hour_position(h, m): #시침 위치 0 <= h < 60 로 표기
    if h >= 12:
        h -= 12
    res = (h * 5) + (m * 5 / 60)
    return (res)

def get_minute_position(m, s):
    res = (m + (s / 60))
    return (res)

def solution(h1, m1, s1, h2, m2, s2):
    midnight_to_sec1 = get_second(h1, m1, s1) # 자정부터 시작시간까지의 초
    midnight_to_sec2 = get_second(h2, m2, s2) # 자정부터 종료시간까지의 초
    count1 = get_count(midnight_to_sec1) # 자정부터 시작시간까지 시계가 움직일 때 알람이 울리는 횟수
    count2 = get_count(midnight_to_sec2) # 자정부터 종료시간까지 시계가 움직일 때 알람이 울리는 횟수
    
    answer = count2 - count1
    
    hour_position = get_hour_position(h1, m1)
    minute_position = get_minute_position(m1, s1)
    if ((s1 == hour_position) or (s1 == minute_position)):
        answer += 1
    
    return answer