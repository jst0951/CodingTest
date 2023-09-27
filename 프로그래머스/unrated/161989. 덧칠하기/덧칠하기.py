def solution(n, m, section):
    count = 1
    start = section[0]
    for s in section:
        if s > start + m - 1:
            start = s
            count += 1
            
    return count