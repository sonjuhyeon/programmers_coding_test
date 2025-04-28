def solution(skill, skill_trees):
    answer = 0
    for i, tree in enumerate(skill_trees):
        tmp = ''
        for char in tree:
            if char in skill:
                tmp += char
        skill_trees[i] = tmp
    
    for tree in skill_trees:
        length = len(tree)
        if skill[:length] == tree:
            answer += 1
    return answer