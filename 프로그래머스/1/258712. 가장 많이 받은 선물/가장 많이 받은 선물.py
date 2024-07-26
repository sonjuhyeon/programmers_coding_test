def solution(friends, gifts):
    answer = 0
    gifts_len = len(gifts)
    friends_len = len(friends)
    gift_idx = {} #선물지수 {이름:선물지수}
    all_case = {} ##모든 경우의 수 {"a b": number} a가 b에게 선물을 더 많이 주었을 때 값은 양수, b가 더 많이 주었을 때는 음수, 0일 때는 주고받지 않았거나 같은 횟수로 주고받은 경우
    all_case_keys = []
    result = {} ## {이름:다음달 받아야 하는 선물 개수}
    
    for i in range(friends_len):
        for j in range(i, friends_len):
            if i != j:
                all_case[friends[i] + " " + friends[j]] = 0 # all_case 초기화
        gift_idx[friends[i]] = 0; #선물지수 초기화
        result[friends[i]] = 0; #결과 초기화
    
    # 선물지수 입력
    for i in range(gifts_len):
        tmp = gifts[i].split(' ')
        gift_idx[tmp[0]] += 1
        gift_idx[tmp[1]] -= 1
        
    ## 개인간의 거래횟수 입력
    for i in range(gifts_len):
        tmp = gifts[i].split(' ')
        rev_tmp = tmp[1] + ' ' + tmp[0]
        if gifts[i] in all_case:
            all_case[gifts[i]] += 1
        elif rev_tmp in all_case:
            all_case[rev_tmp] -= 1
        else:
            rest.append(gifts[i])
    
    all_case_keys = list(all_case.keys())
    
    for i in range(len(all_case_keys)):
        tmp = all_case_keys[i].split(' ')
        if all_case[all_case_keys[i]] > 0:
            result[tmp[0]] += 1
        elif all_case[all_case_keys[i]] < 0:
            result[tmp[1]] += 1
        else:
            if gift_idx[tmp[0]] > gift_idx[tmp[1]]:
                result[tmp[0]] += 1
            if gift_idx[tmp[0]] < gift_idx[tmp[1]]:
                result[tmp[1]] += 1
    
    for i in range(friends_len):
        if answer < result[friends[i]]:
            answer = result[friends[i]]
    
    return answer