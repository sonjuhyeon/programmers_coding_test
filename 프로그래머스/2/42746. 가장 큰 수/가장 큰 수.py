def solution(numbers):
    # 숫자를 문자열로 변환 후, 커스텀 정렬 (반복해서 붙였을 때 더 큰 값이 앞에 오도록 정렬)
    numbers = sorted(map(str, numbers), key=lambda x: x * 3, reverse=True)
    answer = "".join(numbers)
    
    if answer[0] == '0':
        answer = '0'

    return answer
