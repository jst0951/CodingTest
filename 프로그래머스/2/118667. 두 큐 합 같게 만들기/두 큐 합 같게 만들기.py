from collections import deque
def solution(queue1, queue2):
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    count = 0
    while sum_queue1 != sum_queue2:
        count += 1
        if sum_queue1 > sum_queue2:
            popped = queue1.popleft()
            sum_queue1 -= popped
            sum_queue2 += popped
            queue2.append(popped)
        else:
            popped = queue2.popleft()
            sum_queue1 += popped
            sum_queue2 -= popped
            queue1.append(popped)
        
        if len(queue1) == 0 or len(queue2) == 0 or count >= 300000:
            return -1
        
    return count