def get_group(start_box:int, cards:list):
    picked_card_list = []
    picked_card = start_box
    while True:
        picked_card = cards[picked_card-1]
        if picked_card in picked_card_list:
            break
        
        picked_card_list.append(picked_card)
    return picked_card_list

def solution(cards):
    n = len(cards)
    box_list = [i+1 for i in range(n)]
    
    score_list = []
    for start_box_1 in range(1, n+1):
        group_1 = get_group(start_box_1, cards)
        if len(group_1) == n:
            score_list.append(0)
            continue
        
        left_box_list = list(set(box_list[:]) - set(group_1))
        for start_box_2 in left_box_list:
            group_2 = get_group(start_box_2, cards)
            # 점수 계산
            score_list.append(len(group_1) * len(group_2))
    
    return max(score_list)