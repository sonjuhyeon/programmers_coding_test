from math import floor

def solution(players, m, k):
    server = [0] * 24  # 각 시간별 사용 가능한 서버 개수
    answer = 0

    for i in range(len(players)):
        required_server = floor(players[i] / m) # 필요한 서버 개수
        server_to_add = required_server - server[i] # 부족한 서버 개수 계산

        # 추가 서버 필요 없으면 넘어감
        if server_to_add <= 0:
            continue  

        answer += server_to_add # 추가된 서버 개수 증가

        # 추가된 서버를 k시간 동안 유지 (24시간 초과 방지)
        for j in range(i, min(i + k, 24)):  
            server[j] += server_to_add

    return answer
