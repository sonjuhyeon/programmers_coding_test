def solution(id_list, report, k):
    count = {i:0 for i in id_list}
    result = {i:[] for i in id_list}
    mail_count = {i:0 for i in id_list}
    
    for i in set(report):
        a, b = i.split(' ')
        count[b] += 1
        result[b].append(a)
    
    for i,item in count.items():
        if item >= k:
            for j in result[i]: mail_count[j] += 1
            
    return [i for i in mail_count.values()]