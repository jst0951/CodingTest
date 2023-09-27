def solution(wallpaper):
    # 모든 파일들의 위치 검색
    x_list = []
    y_list = []
    for x in range(len(wallpaper)): # x축 좌표
        for y in range(len(wallpaper[x])): # y축 좌표
            if wallpaper[x][y] == '#':
                x_list.append(x)
                y_list.append(y)
    
    return [min(x_list), min(y_list), max(x_list)+1, max(y_list)+1]
        