def solution(park, routes):
    start_pos = [0, 0]
    block_pos_list = []
    x_size = len(park)
    y_size = len(park[0])
    for x in range(len(park)):
        for y in range(len(park[x])):
            if park[x][y] == 'S':
                start_pos[0] = x
                start_pos[1] = y
            elif park[x][y] == 'X':
                block_pos_list.append([x, y])
    print(block_pos_list)
    
    cur_pos = start_pos
    for route in routes:
        way = route[0]
        length = int(route[2:])
        
        # 이동 가능 판별
        if way == 'E':
            # 벗어나는지 판별
            if cur_pos[1] + length >= y_size:
                continue
            # 장애물이 있는지 판별
            for way_pos in [[cur_pos[0], cur_pos[1]+i] for i in range(1, length+1)]:
                is_blocked = False
                for block_pos in block_pos_list:
                    if block_pos[0] == way_pos[0] and block_pos[1] == way_pos[1]:
                        is_blocked = True
                        break
                if is_blocked == True:
                    break
            if is_blocked == True:
                continue
            cur_pos[1] += length
            print('Moved to East,%s' % length)
            
        elif way == 'W':
            # 벗어나는지 판별
            if cur_pos[1] - length < 0:
                continue
            # 장애물이 있는지 판별
            for way_pos in [[cur_pos[0], cur_pos[1]-i] for i in range(1, length+1)]:
                is_blocked = False
                for block_pos in block_pos_list:
                    if block_pos[0] == way_pos[0] and block_pos[1] == way_pos[1]:
                        is_blocked = True
                        break
                if is_blocked == True:
                    break
            if is_blocked == True:
                continue
            cur_pos[1] -= length
            print('Moved to West,%s' % length)
            
        elif way == 'N':
            # 벗어나는지 판별
            if cur_pos[0] - length < 0:
                continue
            # 장애물이 있는지 판별
            for way_pos in [[cur_pos[0]-i, cur_pos[1]] for i in range(1, length+1)]:
                is_blocked = False
                for block_pos in block_pos_list:
                    if block_pos[0] == way_pos[0] and block_pos[1] == way_pos[1]:
                        is_blocked = True
                        break
                if is_blocked == True:
                    break
            if is_blocked == True:
                continue
            cur_pos[0] -= length
            print('Moved to North,%s' % length)

        elif way == 'S':
            # 벗어나는지 판별
            if cur_pos[0] + length >= x_size:
                continue
            # 장애물이 있는지 판별
            for way_pos in [[cur_pos[0]+i, cur_pos[1]] for i in range(1, length+1)]:
                is_blocked = False
                for block_pos in block_pos_list:
                    if block_pos[0] == way_pos[0] and block_pos[1] == way_pos[1]:
                        is_blocked = True
                        break
                if is_blocked == True:
                    break
            if is_blocked == True:
                continue
            cur_pos[0] += length
            print('Moved to South,%s' % length)
            
    return cur_pos