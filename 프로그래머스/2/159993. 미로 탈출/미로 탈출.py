from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 시작 지점(S), 레버 위치(L) 파악
    for x in range(n):
        for y in range(m):
            if maps[x][y] == 'S':
                s_pos = [x, y]
            elif maps[x][y] == 'L':
                l_pos = [x, y]
    
    # 시작 지점에서 레버로 이동
    StartToLever = bfs(s_pos, 'L', maps)
    if StartToLever == -1:
        return -1
    # 레버에서 출구로 이동
    LeverToExit = bfs(l_pos, 'E', maps)
    if LeverToExit == -1:
        return -1
    return StartToLever + LeverToExit
    
    
def bfs(start_pos:list, target_mark:str, arr: list):
    start_x = start_pos[0]
    start_y = start_pos[1]
    
    n = len(arr)
    m = len(arr[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    queue = deque([[start_x, start_y, 0]])
    while queue:
        x, y, count = queue.popleft()
        visited[x][y] = True
        
        if arr[x][y] == target_mark:
            return count
        
        if 0 <= x-1 and visited[x-1][y] == False:
            if arr[x-1][y] != 'X':
                queue.append([x-1, y, count + 1])
                visited[x-1][y] = True
        if 0 <= y-1 and visited[x][y-1] == False:
            if arr[x][y-1] != 'X':
                queue.append([x, y-1, count + 1])
                visited[x][y-1] == True
        if x+1 < n and visited[x+1][y] == False:
            if arr[x+1][y] != 'X':
                queue.append([x+1, y, count + 1])
                visited[x+1][y] = True
        if y+1 < m and visited[x][y+1] == False:
            if arr[x][y+1] != 'X':
                queue.append([x, y+1, count + 1])
                visited[x][y+1] = True
    return -1