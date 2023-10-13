def solution(orig_arr):
    result = []

    arr_list = [orig_arr]
    while arr_list: # arr_list에 남은 arr가 있는 경우
        arr = arr_list.pop()
        n = len(arr)
        
        # 최대한 쪼갰지만 압축불가인 경우
        if n == 1:
            result.append(arr[0][0])
            continue
        # 모든 값이 동일한 경우
        line_arr = []
        for x in range(n):
            for y in range(n):
                line_arr.append(arr[x][y])
        if line_arr.count(0) == n*n:
            result.append(0)
            continue
        elif line_arr.count(1) == n*n:
            result.append(1)
            continue
        # 그렇지 않은 경우, 쪼갠 후 다시 대입
        d = int(n / 2)
        arr_list.append([arr[i][:d] for i in range(d)])
        arr_list.append([arr[i][:d] for i in range(d,n)])
        arr_list.append([arr[i][d:] for i in range(d)])
        arr_list.append([arr[i][d:] for i in range(d,n)])
        
    return [result.count(0), result.count(1)]