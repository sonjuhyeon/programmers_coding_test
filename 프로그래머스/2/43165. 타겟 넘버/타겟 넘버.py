def update_lst(answer_lst, n):
    new_lst = []
    for ans in answer_lst:
        new_lst.append(ans + n)
        new_lst.append(ans - n)
    return new_lst

def solution(numbers, target):
    answer = 0
    answer_lst = []
    for i in range(len(numbers)):
        if i == 0:
            answer_lst.append(numbers[i])
            answer_lst.append(-numbers[i])
        else:
            answer_lst = update_lst(answer_lst, numbers[i])
            
    answer = answer_lst.count(target)
            
    return answer