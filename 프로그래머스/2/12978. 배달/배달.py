from collections import deque

def solution(N, road_list, K):
    city_dict = {} # [연결된 도시, 소요시간]으로 이루어짐
    for road in road_list:
        city_a, city_b, cost = road

        if city_a in city_dict:
            city_dict[city_a].append([city_b, cost])
        else:
            city_dict[city_a] = [[city_b, cost]]
        if city_b in city_dict:
            city_dict[city_b].append([city_a, cost])
        else:
            city_dict[city_b] = [[city_a, cost]]
        
    queue = deque([[1, 0]]) # [현재 도시, 누계소요시간]
    cost_dict = {1:0}
    while queue:
        cur_pos, cur_cost = queue.popleft()
        
        if cur_pos not in city_dict:
            continue
        
        connected_city_list = city_dict[cur_pos]
        for connected_city in connected_city_list:
            target_pos, target_cost = connected_city
            # 아직 가보지 않은 도시인 경우
            if target_pos not in cost_dict:
                cost_dict[target_pos] = cur_cost + target_cost
                queue.append([target_pos, cur_cost + target_cost])
            # 기존 길이 더 돌아가는 길이었던 경우
            elif cost_dict[target_pos] > cur_cost + target_cost:
                cost_dict[target_pos] = cur_cost + target_cost
                queue.append([target_pos, cur_cost + target_cost])
            # 이미 최신 길이었던 경우 큐 츄가 안함.
    
    count = 0
    for city in cost_dict:
        if cost_dict[city] <= K:
            count += 1
    
    return count