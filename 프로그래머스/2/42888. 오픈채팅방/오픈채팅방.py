def solution(record_list):
    result = []
    
    # 각 uuid별로 최종 이름을 저장한 dict
    name_dict = {} # "uid1234" : "Muzi"
    action_list = [] # ["Enter", "Leave", "Change"]
    uuid_list = [] # ["uid1234", "uid4567"]
    name_list = [] # ["Muzi", "Prodo"]
    
    # 입력 변환 기록
    for record in record_list:
        splitted = record.split(' ')
        action_list.append(splitted[0])
        uuid_list.append(splitted[1])
        if len(splitted) == 3:
            name_list.append(splitted[2])
        else:
            name_list.append(None)
    
    # 이름 변경 처리
    for i in range(len(record_list)):
        action = action_list[i]
        if action == "Enter" or action == "Change":
            name_dict[uuid_list[i]] = name_list[i]
    
    # 출력
    for i in range(len(record_list)):
        action = action_list[i]
        uuid = uuid_list[i]
        if action == "Enter":
            result.append("%s님이 들어왔습니다." % name_dict[uuid])
        elif action == "Leave":
            result.append("%s님이 나갔습니다." % name_dict[uuid])
    
    return result