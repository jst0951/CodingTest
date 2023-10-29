from collections import deque

N, r, c = list(map(int, input().split()))

N = 2 ** N
start_pos = 0
while N > 2:
  divsize = int(N * N / 4)
  half_len = int(N / 2)
  if r < half_len and c < half_len:
    start_pos = start_pos + divsize * 0
  elif r < half_len and c >= half_len:
    start_pos = start_pos + divsize * 1
    c -= half_len
  elif r >= half_len and c < half_len:
    start_pos = start_pos + divsize * 2
    r -= half_len
  elif r >= half_len and c >= half_len:
    start_pos = start_pos + divsize * 3
    r -= half_len
    c -= half_len
  N = int(N / 2)
if r == 0 and c == 0:
  print(start_pos + 0)
elif r == 0 and c == 1:
  print(start_pos + 1)
elif r == 1 and c == 0:
  print(start_pos + 2)
elif r == 1 and c == 1:
  print(start_pos + 3)