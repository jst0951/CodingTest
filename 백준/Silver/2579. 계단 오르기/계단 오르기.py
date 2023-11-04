from collections import deque

N = int(input())

step_list = [0]
for _ in range(N):
  step_list.append(int(input()))

queue = deque([[0, 0, 0]]) # 현재 계단, 1개 계단 카운트, 점수

score_history = {}
while queue:
  cur_step, one_count, score = queue.popleft()

  score += step_list[cur_step]
  if cur_step in score_history and one_count in score_history[cur_step]:
    if score_history[cur_step][one_count] < score:
      score_history[cur_step][one_count] = score
    else:
      continue
  elif cur_step in score_history and one_count not in score_history[cur_step]:
    score_history[cur_step][one_count] = score
  elif cur_step not in score_history:
    score_history[cur_step] = {}
    score_history[cur_step][one_count] = score

  
  if cur_step == N:
    continue

  if one_count < 2:
    queue.append([cur_step+1, one_count+1, score])
  if cur_step + 2 <= N:
    queue.append([cur_step+2, 1, score])

print(max(score_history[N].values()))