from collections import deque

N = int(input())
M = int(input())

connected_dict = {}
for _ in range(M):
  com_a, com_b = list(map(int, input().split()))
  
  if com_a in connected_dict:
    connected_dict[com_a].append(com_b)
  else:
    connected_dict[com_a] = [com_b]
  
  if com_b in connected_dict:
    connected_dict[com_b].append(com_a)
  else:
    connected_dict[com_b] = [com_a]
  
visited_dict = {}
for com in connected_dict:
  visited_dict[com] = False

queue = deque([1])

while queue:
  com = queue.popleft()
  visited_dict[com] = True

  if com not in connected_dict:
    continue
  connected_list = connected_dict[com]
  for com in connected_list:
    if com in visited_dict and visited_dict[com] == False:
      queue.append(com)
      visited_dict[com] = True

result_list = [com for com in visited_dict if visited_dict[com] == True]
print(len(result_list) - 1)