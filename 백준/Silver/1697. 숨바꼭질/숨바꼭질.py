from collections import deque

N, K = list(map(int, input().split()))

queue = deque([[N, 0]])
visited = [False for _ in range(400000 + 1)]
min_len = abs(K - N)
while queue:
  cur_pos, elapsed_time = queue.popleft()
  if cur_pos < 0:
    continue

  visited[cur_pos] = True

  if elapsed_time >= min_len:
    continue

  if cur_pos >= K:
    elapsed_time += (cur_pos - K)
    if elapsed_time < min_len:
      min_len = elapsed_time
    continue

  if visited[cur_pos - 1] == False:
    queue.append([cur_pos - 1, elapsed_time + 1])
    visited[cur_pos - 1] = True
  if visited[cur_pos + 1] == False:
    queue.append([cur_pos + 1, elapsed_time + 1])
    visited[cur_pos + 1] = True
  if visited[cur_pos * 2] == False:
    queue.append([cur_pos * 2, elapsed_time + 1])
    visited[cur_pos * 2] = True
  

print(min_len)