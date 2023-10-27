from collections import deque

n = int(input())

number_queue = deque()
for _ in range(n):
    number_queue.append(int(input()))

standby_num = 1
stack_list = []

result_list = []
while number_queue:
    if standby_num <= number_queue[0]:
        stack_list.append(standby_num)
        standby_num += 1
        result_list.append("+")
    elif len(stack_list) > 0 and number_queue[0] == stack_list[-1]:
        stack_list.pop()
        number_queue.popleft()
        result_list.append("-")
    else:
        result_list = ["NO"]
        break

for result in result_list:
    print(result)