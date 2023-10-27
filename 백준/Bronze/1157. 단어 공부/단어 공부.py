word = input().upper()
cnt_dict = {}
for alphabet in word:
    if alphabet in cnt_dict:
        cnt_dict[alphabet] += 1
    else:
        cnt_dict[alphabet] = 1

cnt_list = []
for alphabet in cnt_dict:
    cnt_list.append([alphabet, cnt_dict[alphabet]])

cnt_list.sort(key=lambda x:x[1])
if len(cnt_list) >= 2 and cnt_list[-2][1] == cnt_list[-1][1]:
    print('?')
else:
    print(cnt_list[-1][0])
