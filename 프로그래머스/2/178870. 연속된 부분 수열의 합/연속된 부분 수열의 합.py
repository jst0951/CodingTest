from collections import deque
def solution(sequence, k):
    queue = deque()
    sum_queue = 0
    start_idx = 0
    end_idx = 0
    possible_range_list = [] # [시작 idx, 끝 idx]로 이루어짐
    for idx, number in enumerate(sequence):
        queue.append(number)
        sum_queue += number
        end_idx = idx
        # 같아진 경우
        if sum_queue == k:
            possible_range_list.append([start_idx, end_idx])
            # 다음 경우를 찾기 위해 이동
            start_idx += 1
            sum_queue -= queue.popleft()
        # 더 큰 경우
        elif sum_queue > k:
            while sum_queue > k:
                start_idx += 1
                sum_queue -= queue.popleft()
            # 현재 number가 k와 같은 경우
            if sum_queue == k:
                possible_range_list.append([start_idx, end_idx])
                # 다음 경우를 찾기 위해 이동
                start_idx += 1
                sum_queue -= queue.popleft()
    possible_range_list.sort(key=lambda x:[x[1]-x[0], x[0]])
    return possible_range_list[0]