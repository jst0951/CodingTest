N = int(input())

card_list = list(map(int, input().split()))

M = int(input())

search_list = list(map(int, input().split()))


count_dict = {}
for card in card_list:
  if card in count_dict:
    count_dict[card] += 1
  else:
    count_dict[card] = 1

result_list = []
for search in search_list:
  if search in count_dict:
    result_list.append(count_dict[search])
  else:
    result_list.append(0)

for result in result_list:
  print(result, end=" ")