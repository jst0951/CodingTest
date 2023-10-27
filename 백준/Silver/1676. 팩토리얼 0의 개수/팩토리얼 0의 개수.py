def factorial(n):
    result = 1
    for num in range(1,n+1):
        result *= num
    return result

N = int(input())
char_list = list(str(factorial(N)))
result = 0
for idx in range(len(char_list)-1, -1, -1):
    result += 1
    if char_list[idx] != '0':
        print(result-1)
        break