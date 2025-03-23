from itertools import zip_longest

def get_path(route, points):
    res = []

    for i in range(len(route) - 1):
        start = points[route[i] - 1]
        end = points[route[i + 1] - 1]

        row, col = start
        d_row = 1 if end[0] > row else -1
        d_col = 1 if end[1] > col else -1

        # row 방향으로 먼저 이동
        while row != end[0]:
            res.append([row, col])
            row += d_row

        # col 방향으로 이동
        while col != end[1]:
            res.append([row, col])
            col += d_col

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

def solution(points, routes):
    from collections import defaultdict
    from itertools import zip_longest

    paths = [get_path(route, points) for route in routes]
    # transposed_paths = transpose_matrix(paths)
    transposed_paths = zip_longest(*paths, fillvalue=None)

    answer = 0
    for column in transposed_paths:
        freq = {}
        for val in column:
            if val is None:
                continue
            key = tuple(val)
            freq[key] = freq.get(key, 0) + 1
        answer += sum(1 for cnt in freq.values() if cnt > 1)

    return answer
