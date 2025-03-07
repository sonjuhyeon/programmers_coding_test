def solution(phone_book):
    phone_book.sort()  # 문자열 정렬 (숫자처럼 정렬됨)
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):  # 바로 다음 번호와 비교
            return False
            
    return True
