K, N = list(map(int, input().split()))

cord_list = []
for _ in range(K):
    cord_list.append(int(input()))

max_length = max(cord_list) + 1
min_length = 1
while True:
    test_length = (min_length + max_length) // 2
    if test_length == min_length:
        print(min_length)
        break

    cut_cnt = 0
    for cord in cord_list:
        cut_cnt += (cord // test_length)
    
    if cut_cnt >= N:
        min_length = test_length
    else:
        max_length = test_length