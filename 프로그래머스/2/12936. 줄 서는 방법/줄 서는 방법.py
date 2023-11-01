def pactorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * pactorial(n-1)

def solution(n, k):
    k -= 1

    num_list = list(range(1, n + 1))
    result_list = []
    while n > 1:
        unit = pactorial(n - 1)
        num, k = divmod(k, unit)
        result_list.append(num_list[num])
        num_list.pop(num)
        n -= 1
    result_list.append(num_list[0])
    
    return result_list