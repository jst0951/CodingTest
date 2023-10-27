N, M = list(map(int, input().split()))

board = []
for _ in range(N):
    row = list(input())
    board.append(row)

def diff_chessboard(test_board):
    W_Board = []
    W_Board.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
    W_Board.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
    W_Board.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
    W_Board.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
    W_Board.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
    W_Board.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
    W_Board.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
    W_Board.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])

    W_diff_cnt = 0
    for i in range(8):
        for j in range(8):
            if test_board[i][j] != W_Board[i][j]:
                W_diff_cnt += 1

    return min(W_diff_cnt, 64 - W_diff_cnt)

repaint_cnt_list = []
for x in range((N+1) - 8): # x축 시작점
    for y in range((M+1) - 8): # y축 시작점
        splitted_board = [row[y:y+8] for row in board[x:x+8]]
        repaint_cnt_list.append(diff_chessboard(splitted_board))

print(min(repaint_cnt_list))