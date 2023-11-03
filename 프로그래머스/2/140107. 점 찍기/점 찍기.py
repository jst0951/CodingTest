from math import sqrt

def solution(k, d):
    r_mul_list = list(range(d // k + 1))
    r_list = [k * r_mul for r_mul in r_mul_list]
    
    count = 0
    # 해당 위치에서 최대한 높은 좌표 구하기
    for r in r_list:
        # x좌표는 r로 고정
        y = int(sqrt(d ** 2 - r ** 2))
        count += (y // k + 1) # y가 0일때도 가능
    
    return count