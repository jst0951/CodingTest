from collections import Counter, deque
def solution(topping_list):
    count = 0
    
    # 토핑 종류별 갯수 구하기
    topping_dict = Counter(topping_list)
    
    # 철수가 먹는 토핑 카운트
    first_topping_set = set()
    first_topping_cnt = 0
    for topping in topping_list:
        if topping not in first_topping_set:
            first_topping_set.add(topping)
            first_topping_cnt += 1
        
        topping_dict[topping] -= 1
        if topping_dict[topping] == 0:
            topping_dict.pop(topping)
        second_topping_cnt = len(topping_dict)
        
        if first_topping_cnt == second_topping_cnt:
            count += 1
        
    return count