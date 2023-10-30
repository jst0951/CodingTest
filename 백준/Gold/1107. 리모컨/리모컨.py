from itertools import product

N = int(input())

M = int(input())
if M == 0:
  broken_key_list = []
else:
  broken_key_list = list(map(int, input().split()))

total_key_list = list(range(10))

available_key_list = list(set(total_key_list) - set(broken_key_list))
available_key_str_list = list(map(str, available_key_list))
available_num_list = []
for i in range(1, 7):
  available_num_list.extend(list(product(available_key_str_list, repeat=i)))
available_num_list = [''.join(x) for x in available_num_list]

count_list = [len(x) + abs(int(x) - N) for x in available_num_list]

if len(count_list) > 0:
  count = min(count_list)
else:
  count = 500000

if count > abs(N - 100):
  print(abs(N - 100))
else:
  print(count)