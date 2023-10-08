from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([[0,0]])
    
    while queue:
        node = queue.popleft()
        x = node[0]
        y = node[1]
        
        # 각 방향으로 접근 가능한지, 비방문 상태인지 판별
        move_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for move in move_list:
            dx = move[0]
            dy = move[1]
            if (0 <= (x + dx) and (x + dx) <= n-1) and (0 <= (y + dy) and (y + dy) <= m-1):
                if (maps[x+dx][y+dy] == 1):
                    queue.append([x+dx, y+dy])
                    maps[x+dx][y+dy] = maps[x][y] + 1
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]