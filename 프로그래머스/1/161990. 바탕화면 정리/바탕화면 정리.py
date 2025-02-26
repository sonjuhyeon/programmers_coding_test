def solution(wallpaper):
    # 2차원 배열로 변환
    wallpaper = [list(wallpaper[i]) for i in range(len(wallpaper))]
    
    # 가장 위쪽에 있는 파일의 행 찾기
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            start_row = i
            break
    
    # 가장 아래에 있는 파일의 행 찾기
    for i in range(len(wallpaper) - 1, -1, -1):
        if '#' in wallpaper[i]:
            last_row = i + 1
            break
            
    # 배열 전치
    wallpaper = [list(col) for col in zip(*wallpaper)]
    
    # 가장 왼쪽에 있는 파일의 열 찾기
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            start_col = i
            break
    
    # 가장 오른쪽에 있는 파일의 열 찾기
    for i in range(len(wallpaper) - 1, -1, -1):
        if '#' in wallpaper[i]:
            last_col = i + 1
            break
            
    answer = [start_row, start_col, last_row, last_col]
    return answer