def get_distance(lst, cap):
    farthest = 0
    while lst:
        dis, num = lst.pop()
        if not farthest:
            farthest = dis + 1
        if num > cap:
            num -= cap
            lst.append([dis, num])
            return farthest
        elif num == cap:
            return farthest
        else:
            cap -= num
    return farthest

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveries_list = [[i, deliveries[i]] for i in range(n) if deliveries[i]]
    pickups_list = [[i, pickups[i]] for i in range(n) if pickups[i]]
    
    while deliveries_list or pickups_list:
        delivery_distance = get_distance(deliveries_list, cap)
        pickup_distance = get_distance(pickups_list, cap)
        answer += max(delivery_distance, pickup_distance) * 2

    return answer