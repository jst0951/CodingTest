from collections import deque
def solution(x, y, n):
    result = []
    shortest_dict = {}
    
    queue = deque()
    queue.append([x, 0])
    
    while queue:
        value, count = queue.popleft()
        
        if value in shortest_dict:
            if count < shortest_dict[value]:
                shortest_dict[value] = count
            else:
                continue
        else:
            shortest_dict[value] = count
        
        if value > y:
            continue
        elif value == y:
            result.append(count)
        else:
            count += 1
            if len(result) == 0 or count < min(result):
                queue.append([value*3, count])
                queue.append([value*2, count])
                queue.append([value+n, count])
        
    if len(result) == 0:
        return -1
    else:
        return min(result)