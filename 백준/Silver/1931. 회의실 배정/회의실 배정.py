from collections import deque

N = int(input())

reserve_list = []
used_time_list = []
for _ in range(N):
  start_time, end_time = list(map(int, input().split()))
  reserve_list.append([start_time, end_time, end_time - start_time])

reserve_list.sort(key=lambda x:[x[1], x[0]])

reserve_queue = deque(reserve_list)
count = 0
last_time_used = -1
while reserve_queue:
  start_time, end_time, elapsed_time = reserve_queue.popleft()
  time_range = range(start_time, end_time)
  # 범위 밖인 경우
  if start_time < last_time_used:
    continue

  # 모든 시간이 가용한 경우
  isValid = True
  for time_unit in time_range:
    if time_unit in used_time_list:
      isValid = False
      break
  if isValid == True:
    for time_unit in time_range:
      used_time_list.append(time_unit)
    count += 1
    last_time_used = end_time

print(count)