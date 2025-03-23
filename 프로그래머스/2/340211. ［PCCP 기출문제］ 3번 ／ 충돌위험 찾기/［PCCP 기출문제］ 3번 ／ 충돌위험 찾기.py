from itertools import zip_longest

def get_path(route, points):
    res = []
        
    for i in range(len(route) - 1):
        start, end = points[route[i] - 1], points[route[i + 1] - 1]
        row, col = start[0], start[1]
        
        # row 방향으로 먼저 이동
        for _ in range(abs(start[0] - end[0])):
            res.append([row, col])
            if start[0] < end[0]:
                row += 1
            else:
                row -= 1
                
        # column 방향이동
        for _ in range(abs(start[1] - end[1])):
            res.append([row, col])
            if start[1] < end[1]:
                col += 1
            else:
                col -= 1
        
    res.append([row, col])
            
    return res

# # 열의 길이가 다른 2차원 배열 전치
# def transpose_matrix(matrix):
#     max_len = max(len(row) for row in matrix) # 가장 긴 행의 길이

#     res = []
#     # 열 인덱스를 기준으로 순회
#     for i in range(max_len):
#         transposed_row = []
#         for row in matrix:
#             if i < len(row):
#                 transposed_row.append(row[i])
#             else:
#                 transposed_row.append(None) # 부족한 부분은 None으로 채움
#         res.append(transposed_row)
    
#     return res

def count_duplicates(arr):
    counts = []

    for val in arr:
        if val is None:
            continue  # None은 제외

        found = False
        for i in range(len(counts)):
            if counts[i][0] == val:
                counts[i][1] += 1
                found = True
                break
        if not found:
            counts.append([val, 1])

    # 중복된 값 개수 세기 (2번 이상 등장)
    duplicate_count = 0
    for item, cnt in counts:
        if cnt > 1:
            duplicate_count += 1

    return duplicate_count

def solution(points, routes):
    answer = 0
    paths = []
    
    for route in routes:
        paths.append(get_path(route, points))
        
    # transposed_paths = transpose_matrix(paths)
    transposed_paths = list(zip_longest(*paths, fillvalue=None))
    
    for path in transposed_paths:
        answer += count_duplicates(path)
        
    return answer