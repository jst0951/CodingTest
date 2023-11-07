from itertools import combinations

def isUnique(relation, key):
    # 각 row에 대해 key에 해당하는 col값 조합 추출
    key_data_list = []
    for row in relation:
        data_list = []
        for col in key:
            data_list.append(row[col])

        if data_list not in key_data_list:
            key_data_list.append(data_list)
        else:
            return False
        
    return True

def isMinimal(relation, unique_key_list, test_key):
    # 해당 test_key 하위의 조합이 unique_key_list에 포함되는지 확인
    for key_cnt in range(1, len(test_key)):
        smaller_key_list = list(combinations(test_key, key_cnt))
        for smaller_key in smaller_key_list:
            if list(smaller_key) in unique_key_list:
                return False
    return True

def solution(relation):
    total_row_cnt = len(relation)
    total_col_cnt = len(relation[0])
    
    candidate_key_list = []
    
    # 유일성 확인
    unique_key_list = []
    # 후보키의 컬럼이 1개인 경우부터 검증
    for col_cnt in range(1, total_col_cnt+1):
        # 가능한 조합 파악
        key_list = list(combinations(range(total_col_cnt), col_cnt))
        for key in key_list:
            isUniq = isUnique(relation, key)
            if isUniq == True:
                unique_key_list.append(list(key))
    # 최소성 확인
    for key in unique_key_list:
        isMin = isMinimal(relation, unique_key_list, key)
        if isMin == True:
            candidate_key_list.append(key)
                
    return len(candidate_key_list)