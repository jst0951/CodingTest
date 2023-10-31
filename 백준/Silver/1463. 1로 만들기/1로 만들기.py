from collections import deque

X = int(input())


result_list = []
visited = set()
queue = deque([[X, 0]])
while queue:
  x, count = queue.popleft()
  visited.add(x)
  
  if x == 1:
    result_list.append(count)
    continue

  target_num = int(x / 3)
  if x % 3 == 0 and target_num not in visited :
    queue.append([target_num, count + 1])
    visited.add(target_num)

  target_num = int(x / 2)
  if x % 2 == 0 and target_num not in visited:
    queue.append([target_num, count + 1])
    visited.add(target_num)

  target_num = x - 1
  if target_num not in visited:
    queue.append([target_num, count + 1])
    visited.add(x-1)

print(min(result_list))