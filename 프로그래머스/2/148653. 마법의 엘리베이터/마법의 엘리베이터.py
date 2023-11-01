from collections import deque

def solution(storey):
    count_list = []
    queue = deque([[storey, 0]])
    while queue:
        num, count = queue.popleft()
        num_str = str(num)
        
        if len(num_str) == 1:
            count += min(num, 10 - num + 1)
            count_list.append(count)
            continue
        
        # 가장 낮은 자리수 숫자
        lsb_num = int(num_str[-1])
        # 우로 시프트된(lsb_num이 사라진) 수
        num = int(num_str[:-1])
        
        queue.append([num, count + lsb_num])
        queue.append([num + 1, count + 10 - lsb_num])
    
    return min(count_list)