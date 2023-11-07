from math import sqrt, ceil, floor

def solution(r1, r2):
    cnt = 0
    for x in range(-r2,r2+1):
        y_max = sqrt(r2 ** 2 - x ** 2)
        # x좌표만으로 파란 원 밖인 경우
        if abs(x) >= r1:
            cur_cnt = floor(y_max) * 2 + 1
            cnt += cur_cnt
            continue
        # 파란 원 안에 겹치는 점이 있는 경우
        y_min = sqrt(r1 ** 2 - x ** 2)
        cur_cnt = (floor(y_max) - ceil(y_min) + 1) * 2
        cnt += cur_cnt
    return cnt