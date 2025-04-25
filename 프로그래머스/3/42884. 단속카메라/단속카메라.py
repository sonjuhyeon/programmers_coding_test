def solution(routes):
    answer = 1
    routes.sort()
    camera = routes[0][1]
    print(routes)
    for s, e in routes:
        if s > camera:
            answer += 1
            camera = e
            print(camera)
        camera = min(camera, e)
    return answer