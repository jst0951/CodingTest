N = int(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

# 산술평균
_avg = round(sum(num_list) / len(num_list))
print(_avg)

# 정렬
num_list.sort()

# 중앙값
_mid = num_list[len(num_list) // 2]
print(_mid)

# 최빈값
count_dict = {}
for num in num_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
count_list = []
for num in count_dict:
    count_list.append([num, count_dict[num]])
count_list.sort(key=lambda x: [-x[1], x[0]])
if len(count_list) > 1 and count_list[0][1] == count_list[1][1]:
    _common = count_list[1][0]
else:
    _common = count_list[0][0]
print(_common)

# 범위
_max = max(num_list)
_min = min(num_list)
_range = _max - _min
print(_range)