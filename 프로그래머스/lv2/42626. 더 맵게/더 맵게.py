from heapq import heapify, heappush, heappop

def solution(scoville, K):
    # 최소 값을 반복해서 구해야 합니다.
    # 파이썬의 list의 sort는 O(NlogN)의 시간 복잡도를 가지므로, 느립니다.
    # heapq를 이용하면 O(logN)의 시간 복잡도를 갖도록 구성할 수 있습니다.
    result = 0
    heapify(scoville)
    
    current_min = scoville[0]
    while current_min < K:
        result += 1
        
        if len(scoville) < 2:
            return -1
        min_1st = heappop(scoville)
        min_2nd = heappop(scoville)
        new_food = min_1st + min_2nd * 2
        heappush(scoville, new_food)
        
        current_min = scoville[0]
    
    return result
        