from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    count_list = []
    for x in range(n):
        for y in range(m):
            if visited[x][y] == False:
                count = bfs([x, y], visited, maps)
                if count != 0:
                    count_list.append(count)
    count_list.sort()
    
    if len(count_list) == 0:
        return [-1]
    else:
        return count_list
        
def bfs(start_location, visited, maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([start_location])
    count = 0
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        
        if maps[x][y] == 'X':
            return 0
        else:
            count += int(maps[x][y])
        
        # 우측 가능 파악
        if (y + 1) <= (m - 1) and (maps[x][y+1] != 'X') and (visited[x][y+1] == False):
            queue.append([x, y+1])
            visited[x][y+1] = True
        # 좌측 가능 파악
        if 0 <= (y - 1) and (maps[x][y-1] != 'X') and (visited[x][y-1] == False):
            queue.append([x, y-1])
            visited[x][y-1] = True
        # 하단 가능 파악
        if (x + 1) <= (n - 1) and (maps[x+1][y] != 'X') and (visited[x+1][y] == False):
            queue.append([x+1, y])
            visited[x+1][y] = True
        # 상단 가능 파악
        if 0 <= (x-1) and (maps[x-1][y] != 'X') and (visited[x-1][y] == False):
            queue.append([x-1, y])
            visited[x-1][y] = True
    return count