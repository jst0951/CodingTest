from itertools import combinations
def solution(orders, course):
    orders = [sorted(order) for order in orders]
    
    # course_cnt 개수만큼 선택하여 조합, 가능한 코스 산출
    result_list = [] # 최종 선택된 코스 조합
    for course_cnt in course:
        # 가능한 조합 발견
        possible_course_set = set(combinations(orders[0], course_cnt))
        for i in range(1, len(orders)):
            possible_course_set = possible_course_set | set(combinations(orders[i], course_cnt))
        possible_course_list = list(possible_course_set)
        
        chosen_course_list = [] # [코스, 선택횟수]
        for possible_course in possible_course_list:
            order_cnt = 0
            for order in orders:
                intersection = set(possible_course) & set(order)
                if len(intersection) == course_cnt:
                    order_cnt +=1
            if order_cnt >= 2:
                chosen_course_list.append([possible_course, order_cnt])
        
        # 최대 선택된 조합만 선택
        if len(chosen_course_list) == 0:
            continue
        max_cnt = max([x[1] for x in chosen_course_list])
        for chosen_course in chosen_course_list:
            if chosen_course[1] == max_cnt:
                result_list.append(''.join(sorted(chosen_course[0])))
    
    result_list.sort()
    
    return result_list
    