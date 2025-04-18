def solution(a, b):
    answer = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2016 윤년
    days = sum(month_days[:a - 1]) + b
    return answer[days % 7]