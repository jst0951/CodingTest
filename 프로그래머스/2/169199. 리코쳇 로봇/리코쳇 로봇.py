from collections import deque

def get_movable_position(start_pos:list, direction:str, board:list):
    x, y = start_pos
    n = len(board)
    m = len(board[0])

    # 최대 이동 가능 거리 파악
    if direction == 'DOWN':
        for target_x in range(x, n):
            if board[target_x][y] == 'D':
                return [target_x - 1, y]
        # 맨 끝에 부딪히는 경우
        return [target_x, y]
    elif direction == 'UP':
        for target_x in range(x, -1, -1):
            if board[target_x][y] == 'D':
                return [target_x + 1, y]
        # 맨 끝에 부딪히는 경우
        return [target_x, y]
    elif direction == 'RIGHT':
        for target_y in range(y, m):
            if board[x][target_y] == 'D':
                return [x, target_y - 1]
        # 맨 끝에 부딪히는 경우
        return [x, target_y]
    elif direction == 'LEFT':
        for target_y in range(y, -1, -1):
            if board[x][target_y] == 'D':
                return [x, target_y + 1]
        # 맨 끝에 부딪히는 경우
        return [x, target_y]

def solution(board):
    n = len(board)
    m = len(board[0])
    
    # 시작 위치 R 검색
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                start_pos = [x, y]
    
    # BFS 탐색 시작
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([[start_pos, 0]]) # [[x좌표, y좌표], 카운트]
    while queue:
        start_position, count = queue.popleft()
        x, y = start_position
        visited[x][y] = True
        
        # 목표 도달시 카운트 반환
        if board[x][y] == 'G':
            return count
        
        movable_position_list = []
        movable_position_list.append(get_movable_position([x, y], 'DOWN', board))
        movable_position_list.append(get_movable_position([x, y], 'UP', board))
        movable_position_list.append(get_movable_position([x, y], 'RIGHT', board))
        movable_position_list.append(get_movable_position([x, y], 'LEFT', board))
        for movable_position in movable_position_list:
            # 최대 도달 가능 위치가 현재 위치가 아니고, 방문한 위치가 아닌 경우
            new_x, new_y = movable_position
            if (new_x != x or new_y != y) and visited[new_x][new_y] == False:
                queue.append([[new_x, new_y], count+1])
                visited[new_x][new_y] = True
    # 도달 불가시 -1 return
    return -1