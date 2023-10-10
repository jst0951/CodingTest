def solution(m, n, board):
    board = [list(row) for row in board]
    
    # 총 지운 블록 개수
    total_count = 0
    
    while True:
        # 지운 블록 개수
        count = 0
        
        # 지울 위치 파악
        delete_board = [[False for _ in range(n)] for _ in range(m)]
        for x in range(m-1):
            for y in range(n-1):
                if board[x][y] is not None and board[x][y] == board[x+1][y] and board[x][y] == board[x][y+1] and board[x][y] == board[x+1][y+1]:
                    delete_board[x][y] = True
                    delete_board[x+1][y] = True
                    delete_board[x][y+1] = True
                    delete_board[x+1][y+1] = True
        # 블록 제거
        for x in range(m):
            for y in range(n):
                if delete_board[x][y] == True:
                    board[x][y] = None
                    count += 1
        if count == 0: # 지울 블록이 없는 경우
            break
        else:
            total_count += count

        # 블록 내림
        for y in range(n):
            column = [board[x][y] for x in range(m) if board[x][y] != None]
            while len(column) < m:
                column.insert(0, None)
            for x in range(m):
                board[x][y] = column[x]
    
    return total_count