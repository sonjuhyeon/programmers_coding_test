def solution(enroll, referral, seller, amount):
    graph = {}
    profit_of_member = {}
    for enr, ref in zip(enroll, referral):
        graph[enr] = ref
        profit_of_member[enr] = 0
    
    for sel, amt in zip(seller, amount):
        amt *= 100
        profit_of_member[sel] += amt
        
        while graph[sel] != '-':
            if amt == 0:
                break
            amt = int(amt * 0.1)
            profit_of_member[sel] -= amt
            profit_of_member[graph[sel]] += amt
            
            sel = graph[sel]    
        if graph[sel] == '-':
            profit_of_member[sel] -= int(amt * 0.1)
    
    answer = list(profit_of_member.values())
    return answer