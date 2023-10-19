from collections import deque
def solution(n):
    # 순서 : 1 2 3 4 5 5 5 5 5  4  3  2  3  4  4
    # 값   : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    total_count = int((n/2)*(1+n))
    number_list = deque(range(1, total_count+1))
    row_list = [[0 for _ in range(row_num+1)] for row_num in range(n)]
    
    current_row = 0 # 현재 입력중인 행
    current_col = 0 # 현재 입력중인 열
    highest_row = 0 # 최상단 행
    lowest_row = n-1 # 바닥 행
    while number_list:
        # 대입
        row_list[current_row][current_col] = number_list.popleft()

        # 최하단에 도달한 경우
        if current_row == lowest_row:
            # 아직 최하단 행이 다 차지 않은 경우
            if row_list[lowest_row].count(0) > 0:
                current_col += 1
                continue
            # 다 찬 경우
            else:
                current_row -= 1
                current_col -= 1
                continue
        # 최상단 직전 행에 도달한 경우
        elif current_row == (highest_row + 1):
            # 최상단 직전 행이 가득 찬 경우
            if row_list[current_row].count(0) == 0:
                current_row += 1
                highest_row += 2
                lowest_row -= 1
                continue
        # 내려오고 있는 경우
        if current_col == int(highest_row/2):
            current_row += 1
        # 올라가고 있는 경우
        else:
            current_row -= 1
            current_col -= 1
    result = []
    for row in row_list:
        result.extend(row)
    
    return result