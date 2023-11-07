def solution(k, ranges):
    # 우박수열을 구합니다.
    y_pos_list = []
    n = -1
    while True:
        n += 1
        y_pos_list.append(k)

        if k == 1:
            break
        elif k % 2 == 0:
            k = int(k / 2)
        else:
            k = k * 3 + 1
    
    result_list = []
    for _range in ranges:        
        # 실제 정적분 구간(x축 기준)으로 변환합니다.
        real_range = [_range[0], n+_range[1]]
        
        # 예외처리 : 시작점이 끝점보다 커서 유효하지 않은 경우
        if real_range[0] > real_range[1]:
            result_list.append(-1)
            continue
        
        # 각 정적분값을 구합니다.
        size_sum = 0
        for x in range(real_range[0], real_range[1]):
            size = (y_pos_list[x] + y_pos_list[x+1]) / 2
            size_sum += size
        result_list.append(size_sum)
    return result_list
        