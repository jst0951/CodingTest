from collections import deque


T = int(input())


def bfs(start_pos, cabbage_land, visited):
  queue = deque([start_pos])

  while queue:
    x, y = queue.popleft()
    visited[x][y] = True

    diff_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for diff in diff_list:
      dx, dy = diff
      target_x = x + dx
      target_y = y + dy
      if target_x >= 0 and target_x <= M-1:
        if target_y >= 0 and target_y <= N-1:
          if visited[target_x][target_y] == False and cabbage_land[target_x][target_y] == 1:
            queue.append([target_x, target_y])
            visited[target_x][target_y] = True
    
answer_list = []
for _ in range(T):
  M, N, K = list(map(int, input().split()))
  # M : 가로길이
  # N : 세로길이
  # K : 배추 개수

  # 배추심기
  cabbage_land = [[0 for _ in range(N)] for _ in range(M)]
  for _ in range(K):
    x, y = list(map(int, input().split()))
    cabbage_land[x][y] = 1
  
  # 심어진 배추 파악
  visited = [[False for _ in range(N)] for _ in range(M)]

  count = 0
  for x in range(M):
    for y in range(N):
      if cabbage_land[x][y] == 1 and visited[x][y] == False:
        bfs([x, y], cabbage_land, visited)
        count += 1
  
  answer_list.append(count)

for answer in answer_list:
  print(answer)


