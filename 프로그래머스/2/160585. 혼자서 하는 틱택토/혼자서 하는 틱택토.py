def solution(board):
    # 실수를 한 상황 파악
    
    # 상황 1 : 승리 조건이 여러 번 존재하는 경우
    winner_list = []
    for i in range(3):
        if board[i][0] in ['O', 'X'] and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            winner_list.append(board[i][0])
        if board[0][i] in ['O', 'X'] and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            winner_list.append(board[0][i])
    if board[0][0] in ['O', 'X'] and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        winner_list.append(board[0][0])
    if board[2][0] in ['O', 'X'] and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        winner_list.append(board[2][0])
        
    # 승자가 O, X 모두인 경우
    if len(set(winner_list)) > 1:
        return 0
    elif len(winner_list) > 0:
        winner = winner_list[0]
    else:
        winner = None
        
    # 상황 2 : 둔 수가 특정하지 않는 경우
    O_cnt = 0
    X_cnt = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == 'O':
                O_cnt += 1
            elif board[x][y] == 'X':
                X_cnt += 1
    if O_cnt - X_cnt != 1 and O_cnt - X_cnt != 0:
        return 0
    
    # 상황 3 : 후공이 이겼는데 상대가 계속 둔 경우
    if winner == 'X' and O_cnt > X_cnt:
        return 0
    
    # 상황 4 : 선공이 이겼는데 상대가 계속 둔 경우
    if winner == 'O' and O_cnt <= X_cnt:
        return 0
    
    
    return 1