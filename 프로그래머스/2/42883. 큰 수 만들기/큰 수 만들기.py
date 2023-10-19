from collections import deque
def solution(number, k):
    number_list = list(number)
    stack_list = [] # 앞선 값들의 [값, idx] 모음

    for idx, number in enumerate(number_list):
        while stack_list and k > 0:
            if int(number) > int(stack_list[-1][0]):
                number_list[stack_list[-1][1]] = None # 해당 idx 값 초기화
                stack_list.pop() # stack_list에서 제거
                k -= 1
            else:
                break
                
        if number == '9':
            continue
        elif k == 0:
            break
        else:
            stack_list.append([number, idx])
            stack_list.sort(key = lambda x:[-int(x[0]), x[1]])
            
        
    result_list = [x for x in number_list if x is not None]
    if k != 0:
        result_list = result_list[:-k]
    return ''.join(result_list)