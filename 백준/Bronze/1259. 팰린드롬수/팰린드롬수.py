result_list = []
while True:
    input_str = input()
    if input_str == '0':
        break

    isValid = True
    for i in range(len(input_str) // 2):
        if input_str[i] != input_str[-i - 1]:
            isValid = False
            break
    
    if isValid == True:
        result_list.append("yes")
    else:
        result_list.append("no")

for result in result_list:
    print(result)