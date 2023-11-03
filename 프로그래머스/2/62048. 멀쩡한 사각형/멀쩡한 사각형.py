from math import ceil, floor, gcd

def solution(w,h):
    # 연산 제외
    if w == h:
        return w*h - h
    elif w == 1 or h == 1:
        return 0
    
    count = 0
    
    # n : 동일한 패턴이 반복되기까지의 col 길이
    _gcd = gcd(w,h)
    n = int(w / _gcd)
    
    for i in range(0, n):
        start = floor(h * i / w)
        end = ceil(h * (i+1) / w)
        
        count += end - start
    
    return (w * h) - (count * _gcd)