def solution(data, col, row_begin, row_end):
    
    # 정렬
    data.sort(key=lambda x:[x[col-1], -x[0]])
    
    # S_i 수집
    s_list = []
    for i in range(row_begin, row_end+1):
        row = data[i-1]
        mod_reesult = [val % i for val in row]
        s_list.append(sum(mod_reesult))
    
    # 해시 값
    hashval = s_list[0]
    for i in range(1, len(s_list)):
        hashval ^= s_list[i]
    
    return hashval