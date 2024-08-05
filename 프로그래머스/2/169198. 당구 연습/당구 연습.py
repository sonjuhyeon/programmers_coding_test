def get_distance(size, start, end, the_other_start, end_ball):
    dis1 = start + end
    dis2 = (size - start) + (size - end)
    if (the_other_start == end_ball):
        if (start > end):
            return (dis2)
        else:
            return (dis1)
    if (dis1 < dis2):
        return (dis1)
    else:
        return (dis2)
    

def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        x_dis1 = abs(ball[0] - startX)
        y_dis1 = get_distance(n, startY, ball[1], startX, ball[0])
        dis1 = (x_dis1 ** 2) + (y_dis1 ** 2)
        
        x_dis2 = get_distance(m, startX, ball[0], startY, ball[1])
        y_dis2 = abs(ball[1] - startY)
        dis2 = (x_dis2 ** 2) + (y_dis2 ** 2)
        
        if (dis1 < dis2):
            answer.append(dis1)
        else:
            answer.append(dis2)
        
    return answer