def solution(board):
    n = len(board)
    m = len(board[0])
# 구현
#     max_length = min(n, m)
    
#     for length in range(max_length, 0, -1):
#         for x_start in range(0, n - length + 1):
#             for y_start in range(0, m - length + 1):
#                 test_board = [row[y_start:y_start + length] for row in board[x_start:x_start + length]]
#                 isSquare = True
#                 for row in test_board:
#                     for item in row:
#                         if item == 0:
#                             isSquare = False
#                             break
#                 if isSquare == True:
#                     return length ** 2
    
#     return 0

# DP
    for x in range(1, n):
        for y in range(1, m):
            if board[x][y] != 0:
                board[x][y] = min(board[x-1][y-1], board[x-1][y], board[x][y-1]) + 1
    max_list = [max(row) for row in board]
    return max(max_list) ** 2