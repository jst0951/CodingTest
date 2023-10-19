def solution(n):
    result = ''
    while n > 0:
        n, mod = divmod(n-1, 3)
        if mod == 0:
            result += '1'
        elif mod == 1:
            result += '2'
        elif mod == 2:
            result += '4'
    
    result = result[::-1]
    return result