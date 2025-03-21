from math import log

def complete_binary_tree(binary):
    n_len = len(binary)
    
    number_of_node = 1 # 완전이진트리가 되기 위한 node 개수
    while n_len >= number_of_node:
        number_of_node *= 2
    number_of_node -= 1 # (N^2)-1
    
    for i in range(number_of_node - n_len):
        binary = '0' + binary
    return binary

# 완전이진트리 형태가 가능한지 확인
def check_complete_binary_tree(binary_n):
    level = log(len(binary_n) + 1, 2) - 1
    
    for i in range(int(level)):
        root_node = int(2 ** (level - i))
        for j in range(root_node, root_node + (root_node * 2) * (2 ** i), (root_node * 2)):
            start = j - root_node
            end = j + root_node - 1
            if (binary_n[j - 1] == '0') and ('1' in binary_n[start:end]):
                return 0
    return 1
        
def solution(numbers):
    answer = []
    for n in numbers:
        binary_n = bin(n)[2:]
        binary_n = complete_binary_tree(binary_n) # 완전 이진 트리가 되도록 '0'추가
        answer.append(check_complete_binary_tree(binary_n))
    return answer
