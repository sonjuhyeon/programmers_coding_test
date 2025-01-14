from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    term = {}
    today = datetime.strptime(today,'%Y.%m.%d')
    
    for t in terms:
        doc_type, month = t.split(" ")
        term[doc_type] = int(month)
    print(term)
        
    for idx, pri in enumerate(privacies):
        date, sort = pri.split(" ")
        date = datetime.strptime(date,'%Y.%m.%d')
        diff = [(today.year-date.year)*12 + today.month-date.month, today.day - date.day]
        if diff[1] < 0 : # day 차이가 음수라면 1개월을 day로 전환.
            diff[0] -= 1
            diff[1] += 28
        if diff[0] >= term[sort]: 
            answer.append(idx+1)
        
    return answer