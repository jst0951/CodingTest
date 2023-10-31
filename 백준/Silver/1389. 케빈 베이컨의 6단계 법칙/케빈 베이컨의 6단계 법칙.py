from collections import deque

N, M = list(map(int, input().split()))

friend_dict = {}
for _ in range(M):
  a, b = list(map(int, input().split()))

  if a in friend_dict:
    friend_dict[a].append(b)
  else:
    friend_dict[a] = [b]
  if b in friend_dict:
    friend_dict[b].append(a)
  else:
    friend_dict[b] = [a]

def get_friend_score(friend_dict: dict, start_person: int, end_person: int):
  count_list = []

  visited_dict = {}
  for key in friend_dict:
    visited_dict[key] = False
  
  queue = deque([[start_person, 0]]) # 사람번호, 카운트
  while queue:
    person, count = queue.popleft()
    visited_dict[person] = True

    if person == end_person:
      count_list.append(count)
      continue

    target_person_list = friend_dict[person]
    for target_person in target_person_list:
      if visited_dict[target_person] == False:
        queue.append([target_person, count + 1])
        visited_dict[target_person] = True

  return min(count_list)
  
result_list = []
for person_num in friend_dict:
  friend_num_list = [x for x in friend_dict.keys() if x != person_num]
  score = 0
  for friend_num in friend_num_list:
    score += get_friend_score(friend_dict, person_num, friend_num)
  result_list.append([person_num, score])
result_list.sort(key=lambda x:x[1])

if len(result_list) >= 2 and result_list[0][1] == result_list[1][1]:
  print(min(result_list[0][0], result_list[1][0]))
else:
  print(result_list[0][0])