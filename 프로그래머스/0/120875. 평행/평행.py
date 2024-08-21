def solution(dots):
    ratio = {}
    for i in range(3):
        for j in range(i, 3):
            x_dis = dots[i][0] - dots[j + 1][0]
            y_dis = dots[i][1] - dots[j + 1][1]
            tmp = (y_dis / x_dis)
            if tmp in ratio:
                if [dots[i][0], dots[i][1]] in ratio[tmp]:
                    continue
                return 1
            ratio[tmp] = [[dots[i][0], dots[i][1]], [dots[j + 1][0], dots[j + 1][1]]]
            print(ratio[tmp][0], ratio[tmp][1])
    answer = 0
    return answer