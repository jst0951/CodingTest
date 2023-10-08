def solution(skill_order, skill_trees):
    count = 0
    
    # 필수 스킬트리만 추출
    vital_skill_tree_list = []
    for skill_tree in skill_trees:
        skill_tree_list = list(skill_tree)
        for i in range(len(skill_tree_list)):
            if skill_tree_list[i] not in skill_order:
                skill_tree_list[i] = ''
        vital_skill_tree = ''.join([x for x in skill_tree_list if x != ''])
        vital_skill_tree_list.append(vital_skill_tree)
    print(vital_skill_tree_list)
    
    # 가능한 순서 추출
    available_skill_tree_list = []
    for i in range(len(skill_order)):
        available_skill_tree_list.append(skill_order[:i+1])
    print(available_skill_tree_list)

    # 비교
    for vital_skill_tree in vital_skill_tree_list:
        if vital_skill_tree == '':
            count += 1
            continue
        for available_skill_tree in available_skill_tree_list:
            if vital_skill_tree == available_skill_tree:
                count += 1
                break
    
    return count