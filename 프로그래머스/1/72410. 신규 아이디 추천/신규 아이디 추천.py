def solution(new_id):
    new_id = new_id.lower()
    new_id = list(new_id)
    
    for i in range(len(new_id) - 1, -1, -1):
        if not (new_id[i].islower() or
                new_id[i].isdigit() or
                new_id[i] in ['-', '_', '.']):
            new_id.pop(i)
    
    for i in range(len(new_id) - 1, -1, -1):
        if new_id[i] == '.' and new_id[i - 1] == '.' and i != 0:
            new_id.pop(i)
            
    # print(new_id)
    
    if new_id[0] == '.':
        new_id.pop(0)
    if not new_id:
        new_id.append('a')
    if len(new_id) > 15:
        new_id = new_id[0:15]
    if new_id[-1] == '.':
        new_id.pop()
    if len(new_id) < 3:
        for i in range(len(new_id) - 1, 2):
            new_id.append(new_id[i])
        
    # print(new_id)
    
    answer = ''.join(new_id)
    return answer