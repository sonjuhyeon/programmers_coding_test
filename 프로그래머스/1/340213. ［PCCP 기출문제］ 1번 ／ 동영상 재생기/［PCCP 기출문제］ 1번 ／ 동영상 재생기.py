def solution(video_len, pos, op_start, op_end, commands):
    # 비디오 길이
    v_mm, v_ss = map(int, video_len.split(":"))

    # 현재 위치
    cur_mm, cur_ss = map(int, pos.split(":"))

    # 오프닝 시작과 끝 위치
    ops_mm, ops_ss = map(int, op_start.split(":"))
    ope_mm, ope_ss = map(int, op_end.split(":"))
    
    # 명령을 수행하기 전에 오프닝 구간인지 확인하고 건너뛰기
    if (ops_mm * 60 + ops_ss) <= (cur_mm * 60 + cur_ss) <= (ope_mm * 60 + ope_ss):
        cur_mm, cur_ss = ope_mm, ope_ss

    for c in commands:
        # 명령을 수행하기 전에 오프닝 구간인지 확인하고 건너뛰기
        if (ops_mm * 60 + ops_ss) <= (cur_mm * 60 + cur_ss) <= (ope_mm * 60 + ope_ss):
            cur_mm, cur_ss = ope_mm, ope_ss

        # prev - 10초 전으로 이동
        if c == 'prev':
            if cur_ss >= 10:
                cur_ss -= 10
            elif cur_mm == 0:
                cur_mm, cur_ss = 0, 0
            else:
                cur_mm -= 1
                cur_ss = 60 - (10 - cur_ss)  # 10초 전으로 이동

        # next - 10초 후로 이동
        else:
            if cur_ss < 50:
                cur_ss += 10
            else:
                cur_mm += 1
                cur_ss -= 50
            if cur_mm >= v_mm and cur_ss >= v_ss:
                cur_mm, cur_ss = v_mm, v_ss

    # 명령이 모두 끝난 후, 마지막으로 오프닝 구간인지 확인
    if (ops_mm * 60 + ops_ss) <= (cur_mm * 60 + cur_ss) <= (ope_mm * 60 + ope_ss):
        cur_mm, cur_ss = ope_mm, ope_ss

    # mm:ss 형식으로 반환
    if cur_mm < 10: mm = '0' + str(cur_mm)
    else: mm = str(cur_mm)

    if cur_ss < 10: ss = '0' + str(cur_ss)
    else: ss = str(cur_ss)

    return mm + ":" + ss
