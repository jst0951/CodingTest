import heapq

result_list = []

heap = []
N = int(input())
for _ in range(N):
  x = int(input())
  if x == 0:
    if len(heap) == 0:
      result_list.append(0)
    else:
      result_list.append(heapq.heappop(heap))
  else:
    heapq.heappush(heap, x)

for result in result_list:
  print(result)