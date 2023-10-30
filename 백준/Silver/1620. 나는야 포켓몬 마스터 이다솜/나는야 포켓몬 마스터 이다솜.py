N, M = list(map(int, input().split()))

name_dict = {}
number_dict = {}
for number in range(1, N+1):
  name = input()
  name_dict[number] = name
  number_dict[name] = number

result_list = []
for _ in range(M):
  input_str = input()
  if input_str.isdigit():
    result_list.append(name_dict[int(input_str)])
  else:
    result_list.append(number_dict[input_str])

for result in result_list:
  print(result)