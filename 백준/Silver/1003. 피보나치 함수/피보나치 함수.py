T = int(input())

fibo_list = [0, 1]
one_list = [0, 1]
zero_list = [1, 0]
def fibonnacci(n):
    while len(fibo_list) <= n:
        fibo_list.append(fibo_list[-2] + fibo_list[-1])
        one_list.append(one_list[-2] + one_list[-1])
        zero_list.append(zero_list[-2] + zero_list[-1])
    
    return fibo_list[n]
    
num_list = []
for _ in range(T):
    num_list.append(int(input()))

max_num = max(num_list)
fibonnacci(max_num)

for num in num_list:
    print("%s %s" % (zero_list[num], one_list[num]))