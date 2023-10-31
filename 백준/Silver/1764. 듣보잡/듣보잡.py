N, M = list(map(int, input().split()))

non_heard_set = set()
for _ in range(N):
  non_heard_set.add(input())

non_seen_set = set()
for _ in range(M):
  non_seen_set.add(input())

non_ever_list = list(non_heard_set & non_seen_set)
print(len(non_ever_list))
non_ever_list.sort()
for person in non_ever_list:
  print(person)