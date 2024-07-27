def res_idx(s):
    if s == 'code':
        return (0)
    elif s == 'date':
        return (1)
    elif s == 'maximum':
        return (2)
    else:
        return (3)

def sort(data, idx):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i][idx] > data[j][idx]:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
                
    
def solution(data, ext, val_ext, sort_by):
    # data[code(코드번호), date(제조일), maximum(최대수량), remain(현재수량)]
    
    ext_idx = res_idx(ext)
    sort_idx = res_idx(sort_by)
    data_len = len(data)
    remove_lst = []
    
    for i in range(data_len):
        if data[i][ext_idx] >= val_ext:
            remove_lst.append(data[i])
            
    for i in remove_lst:
        data.remove(i)
    
    data_len = len(data)
    sort(data, sort_idx)
    
    answer = data
    return answer