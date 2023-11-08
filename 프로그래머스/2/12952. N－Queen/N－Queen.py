from collections import deque

def solution(n):
    queue = deque([]) # [[사용된 열 목록], 카운트]
    for start_col in range(n):
        queue.append([[start_col], 1])
    
    result = 0
    while queue:
        used_col_list, count = queue.popleft()

        if count == n:
            result += 1
            continue
        
        # 다음 열 선택이 가능한 목록 파악
        cur_row = len(used_col_list)
        unusable_col_list = []
        for i in range(cur_row):
            unusable_col_list.append(used_col_list[i] - (cur_row - i))
            unusable_col_list.append(used_col_list[i])
            unusable_col_list.append(used_col_list[i] + (cur_row - i))
        next_col_list = set(range(n)) - set(unusable_col_list)

        # 방문 가능한 열 방문
        for next_col in next_col_list:
            queue.append([used_col_list + [next_col], count + 1])
    
    return result