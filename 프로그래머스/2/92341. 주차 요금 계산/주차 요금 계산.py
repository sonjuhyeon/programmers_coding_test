from collections import defaultdict

def get_parking_time(start, end):
    result = 0
    start_h, start_m = start.split(':')
    end_h, end_m = end.split(':')
    start_h, start_m, end_h, end_m = int(start_h), int(start_m), int(end_h), int(end_m)
    
    result += (end_h - start_h) * 60
    result += end_m - start_m
    
    return result

def get_fee(fees, parking_time):
    # fees [기본시간(분), 기본요금, 단위시간(분), 단위 요금]
    result = 0
    if fees[0] >= parking_time:
        return fees[1]
    else:
        result += fees[1]
        parking_time -= fees[0]
    if parking_time % fees[2] == 0:
        result += (parking_time // fees[2]) * fees[3]
    else:
        result += (parking_time // fees[2] + 1) * (fees[3])
    return result

def solution(fees, records):
    answer = []
    cars_io = defaultdict(list) # 출입차 시간
    parking_time = defaultdict(int) # 누적 주차 시간
    for record in records:
        time, car_num, io = record.split(' ')
        cars_io[car_num].append(time)
        if io == "OUT":
            parking_time[car_num] += get_parking_time(cars_io[car_num][-2], time)
    
    for car_num in cars_io:
        if len(cars_io[car_num]) % 2 == 1:
            parking_time[car_num] += get_parking_time(cars_io[car_num][-1], "23:59")
    
    for car_num in sorted(parking_time.keys()):
        answer.append(get_fee(fees, parking_time[car_num]))
    return answer
