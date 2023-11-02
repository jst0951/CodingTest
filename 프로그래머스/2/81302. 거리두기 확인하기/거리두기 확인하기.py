from collections import deque

def check_valid(start_location, place):
    x_start, y_start = start_location
    queue = deque([[x_start, y_start, False, 0]]) # [x위치, y위치, 상태(경로에 빈 테이블이 있는 경우 True), 방문카운트]로 설정
    
    while queue:
        x, y, isEmptyTableOnRoute, count = queue.popleft()
        
        if place[x][y] == 'O':
            isEmptyTableOnRoute = True
        
        if place[x][y] == 'P' and count == 1:
            return False
        
        if place[x][y] == 'P' and isEmptyTableOnRoute == True:
            return False
        
        if count == 2:
            continue
        
        if 0 <= x-1 and x-1 <= 4 and x-1 != x_start:
            queue.append([x-1, y, isEmptyTableOnRoute, count + 1])

        if 0 <= y-1 and y-1 <= 4 and y-1 != y_start:
            queue.append([x, y-1, isEmptyTableOnRoute, count + 1])

        if 0 <= x+1 and x+1 <= 4 and x+1 != x_start:
            queue.append([x+1, y, isEmptyTableOnRoute, count + 1])

        if 0 <= y+1 and y+1 <= 4 and y+1 != y_start:
            queue.append([x, y+1, isEmptyTableOnRoute, count + 1])

    return True

def solution(places):
    answer_list = []
    
    for place in places:
        # P의 위치 파악
        p_location_list = []
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    p_location_list.append([x, y])
        
        # 각 P에 대해 탐색 가능한 위치 파악
        isValid = True
        for p_location in p_location_list:
            result = check_valid(p_location, place)
            if result == False:
                isValid = False
                break
        if isValid == True:
            answer_list.append(1)
        else:
            answer_list.append(0)
    
    return answer_list


                