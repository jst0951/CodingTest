def solution(rows, columns, queries):
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    count = 0
    for x in range(rows):
        for y in range(columns):
            count += 1
            arr[x][y] = count
            
    answer_list = [] # 위치 변경 숫자들 중 가장 작은 숫자
    for query in queries:
        # 연산 대상 좌표 목록
        target_list = [] # [[x좌표, y좌표], 값]으로 구성
        x1, y1, x2, y2 = query
        # 0부터 시작하는 좌표계로 변환
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x == x1 or x == x2 or y == y1 or y == y2:
                    target_list.append([[x, y], arr[x][y]])
        # 쉬프트 후 연산 결과
        result_list = []
        for target in target_list:
            x, y = target[0]
            value = target[1]
            # 좌측 상단 모서리
            if x == x1 and y == y1:
                y += 1
            # 우측 상단 모서리
            elif x == x1 and y == y2:
                x += 1
            # 좌측 하단 모서리
            elif x == x2 and y == y1:
                x -= 1
            # 우측 하단 모서리
            elif x == x2 and y == y2:
                y -= 1
            # 최상단 row
            elif x == x1:
                y += 1
            # 최하단 row
            elif x == x2:
                y -= 1
            # 최좌단 col
            elif y == y1:
                x -= 1
            # 최우단 col
            elif y == y2:
                x += 1
            result_list.append([[x, y], value])
        min_value = min([result[1] for result in result_list])
        answer_list.append(min_value)
        
        # 실제 변경 적용
        for result in result_list:
            x, y = result[0]
            value = result[1]
            arr[x][y] = value
    return answer_list