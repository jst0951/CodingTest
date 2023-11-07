from collections import deque

def solution(plans):
    playtime_dict = {} # 과제별 소요시간
    plan_list = []
    for plan in plans:
        name, start, playtime = plan
        start_timestamp = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
        playtime_dict[name] = int(playtime)
        plan_list.append([name, start_timestamp])
    plan_list.sort(key=lambda x:x[1])
    
    result_list = []
    
    queue = deque(plan_list)
    stack = [] # [name, time_spent]
    cur_time = queue[0][1]
    while len(queue) > 0 or len(stack) > 0:
        # 과제를 시작하기로 한 시각이 되면 시작
        if len(queue) > 0 and cur_time == queue[0][1]:
            name, start_timestamp = queue.popleft()
            # 스택의 맨 마지막에 저장
            stack.append([name, 0])
            
        # 현재 시간에 진행할 과제가 없으면 다음 과제 시간까지 이동
        if len(stack) == 0:
            cur_time = queue[0][1]
            continue
        # 진행중인 과제가 있으면 과제 진행
        stack[-1][1] += 1
        # 해당 과제에 필요한 시간을 사용했으면 과제 종료
        if stack[-1][1] >= playtime_dict[stack[-1][0]]:
            name, start_timestamp = stack.pop()
            result_list.append(name)
            
        # 시간 소요 처리
        cur_time += 1
    return result_list