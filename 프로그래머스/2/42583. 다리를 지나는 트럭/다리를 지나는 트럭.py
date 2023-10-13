from collections import deque
def solution(bridge_length, weight, truck_weights):
    result = 0
    
    wait_queue = deque(truck_weights)
    bridge_queue = deque()
    count_queue = deque()

    while len(wait_queue) > 0 or len(bridge_queue) > 0:
        result += 1
        
        # 올라온 트럭들 카운트 갱신
        for i in range(len(bridge_queue)):
            count_queue[i] += 1
        # 다리를 다 지난 경우 pop
        while bridge_queue:
            if count_queue[0] == bridge_length:
                bridge_queue.popleft()
                count_queue.popleft()
            else:
                break
        
        # 트럭 다리 위에 올리기
        if len(wait_queue) > 0 and sum(bridge_queue) + wait_queue[0] <= weight:
            bridge_queue.append(wait_queue.popleft())
            count_queue.append(0)
            
    return result