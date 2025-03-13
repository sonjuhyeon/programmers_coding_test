def solution(brown, yellow):
    answer = []
    n_grid = brown + yellow
    for h in range(3, n_grid // 2):
        if n_grid % h == 0:
            w = n_grid // h
            n_brown = (h * 2) + (w - 2) * 2
            if n_brown == brown:
                answer = [w, h]
                break
    return answer