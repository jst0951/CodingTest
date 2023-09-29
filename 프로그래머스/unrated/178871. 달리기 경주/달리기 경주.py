def solution(players, callings):
    # 현재 순위 조회를 빠르게 하기 위한 dict 생성
    rank_dict = {}
    for i in range(len(players)):
        rank_dict[players[i]] = i
    
    for calling in callings:
        # 불린 사람의 현재 순위를 dict를 통해 빠르게 찾기
        current_idx = rank_dict[calling]
        
        # 앞에 있던 사람 찾기
        front_player = players[current_idx-1]
        
        # 순서 뒤집기(dict)
        rank_dict[calling] -= 1
        rank_dict[front_player] += 1
        
        # 실제 list에도 반영
        players[current_idx-1] = calling
        players[current_idx] = front_player
    
    return players
    
        