from collections import deque

def solution(n, wires):
    diff_list = [] # 송전탑 개수 차이를 담을 list
    for i in range(len(wires)):
        # 끊을 와이어 선택
        disconnect_wire = wires[i]
        # 남은 와이어 목록
        left_wire_list = [wire for idx, wire in enumerate(wires) if idx != i]
        
        # 연결 정보 포함한 dict 생성
        wire_dict = {}
        for left_wire in left_wire_list:
            com_a, com_b = left_wire
            if com_a in wire_dict:
                wire_dict[com_a].append(com_b)
            else:
                wire_dict[com_a] = [com_b]
            if com_b in wire_dict:
                wire_dict[com_b].append(com_a)
            else:
                wire_dict[com_b] = [com_a]
        
        # 한 쪽에 남은 송전탑 개수 카운트
        left_1 = get_count(wire_dict, list(wire_dict.keys())[0])
        # 나머지 송전탑 개수 및 차 연산
        left_2 = n - left_1
        diff_list.append(abs(left_1 - left_2))
        
    return min(diff_list)
        
def get_count(wire_dict: dict, start_pos: int):
    queue = deque([start_pos])
    count = 1
    
    visited_dict = {}
    for wire in wire_dict:
        visited_dict[wire] = False
    
    while queue:
        current_wire = queue.popleft()
        visited_dict[current_wire] = True
        
        if current_wire not in wire_dict:
            continue
    
        connected_wire_list = wire_dict[current_wire]
        for connected_wire in connected_wire_list:
            if visited_dict[connected_wire] == False:
                queue.append(connected_wire)
                visited_dict[connected_wire] = True
                count += 1
    return count
    