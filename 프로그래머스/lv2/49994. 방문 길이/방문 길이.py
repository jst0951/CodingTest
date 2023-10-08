def solution(direction_list):
    history_list = []
    position = [0, 0]
    count = 0
    for direction in direction_list:
        if direction == 'U':
            diff = [0, 1]
        elif direction == 'D':
            diff = [0, -1]
        elif direction == 'R':
            diff = [1, 0]
        elif direction == 'L':
            diff = [-1, 0]
        if position[0] + diff[0] < -5 or position[0] + diff[0] > 5 or position[1] + diff[1] < -5 or position[1] + diff[1] > 5:
            continue
        new_position = [position[0] + diff[0], position[1] + diff[1]]
        
        isNew = True
        for history in history_list:
            if (history[0] == position[0] and history[1] == position[1] and history[2] == new_position[0] and history[3] == new_position[1]) or (history[0] == new_position[0] and history[1] == new_position[1] and history[2] == position[0] and history[3] == position[1]):
                isNew = False
                break
        if isNew == True:
            count += 1
            history_list.append(position + new_position)
            
        position = new_position
    return count