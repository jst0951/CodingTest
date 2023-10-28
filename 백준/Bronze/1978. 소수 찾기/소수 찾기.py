def isPrime(num):
    if num == 1:
        return False
    
    for x in range(2, num):
        if num % x == 0:
            return False
    
    return True

N = int(input())
num_list = list(map(int, input().split()))

count = 0
for num in num_list:
    if isPrime(num) == True:
        count += 1

print(count)