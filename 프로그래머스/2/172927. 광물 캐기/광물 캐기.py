from collections import deque
from itertools import permutations

pick_list = ["diamond", "iron", "stone"]
pick_idx_dict = {"diamond":0, "iron":1, "stone":2}

def solution(picks, minerals):
    cost_dict = {}
    for mineral in pick_list:
        cost_dict[mineral] = {}
    cost_dict["diamond"]["diamond"] = 1
    cost_dict["diamond"]["iron"] = 1
    cost_dict["diamond"]["stone"] = 1
    cost_dict["iron"]["diamond"] = 5
    cost_dict["iron"]["iron"] = 1
    cost_dict["iron"]["stone"] = 1
    cost_dict["stone"]["diamond"] = 25
    cost_dict["stone"]["iron"] = 5
    cost_dict["stone"]["stone"] = 1
    
    cost_list = []
    queue = deque([]) # 이번 채굴에 사용할 곡괭이, 남은 곡괭이 목록, 남은 광물 큐, 사용 내구도 카운트
    for start_pick in pick_list:
        # 해당 곡괭이가 있는 경우에만
        if picks[pick_idx_dict[start_pick]] > 0:
            left_pick_list = picks[:]
            left_mineral_queue = deque(minerals)
            queue.append([start_pick, left_pick_list, left_mineral_queue, 0])
    
    count_list = []
    while queue:
        pick, left_pick_list, left_mineral_queue, count = queue.popleft()
        
        # 채굴 진행
        for _ in range(5):
            mineral = left_mineral_queue.popleft()
            count += cost_dict[pick][mineral]
            # 5번 채굴 전에 채굴이 끝난 경우
            if len(left_mineral_queue) == 0:
                break
        left_pick_list[pick_idx_dict[pick]] -= 1
        
        # 남은 채굴할 광석이 없거나, 곡괭이가 남지 않은 경우
        if len(left_mineral_queue) == 0 or sum(left_pick_list) == 0:
            count_list.append(count)
            continue
        
        # 남은 곡괭이로 채굴 시도
        for idx in range(len(left_pick_list)):
            if left_pick_list[idx] > 0:
                pick = pick_list[idx]
                queue.append([pick, left_pick_list[:], deque(left_mineral_queue), count])
    
    return min(count_list)