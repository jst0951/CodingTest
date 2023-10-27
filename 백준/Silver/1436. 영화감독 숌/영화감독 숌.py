N = int(input())

count = 0
for num in range(666, 1000000000000):
    if '666' in str(num):
        count += 1
        if count == N:
            print(num)
            break
        