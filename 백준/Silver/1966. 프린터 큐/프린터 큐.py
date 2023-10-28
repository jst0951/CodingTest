from collections import deque
T = int(input())

result_list = []
for _ in range(T):
    N, M = list(map(int, input().split()))
    priority_deque = deque(list(map(int, input().split())))

    interest_idx = M
    count = 0
    while priority_deque:
        max_priority = max(priority_deque)
        while priority_deque[0] != max_priority:
            interest_idx -= 1
            priority_deque.append(priority_deque.popleft())
        if interest_idx < 0:
            interest_idx += len(priority_deque)
        
        # 가장 높은 우선도 문서 출력
        priority_deque.popleft()
        count += 1
        if interest_idx == 0:
            result_list.append(count)
            break
        else:
            interest_idx -= 1

for result in result_list:
    print(result)