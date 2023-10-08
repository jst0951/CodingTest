def solution(numbers):
    stack = [] # 뒷 큰수를 찾지 못한 값들 저장, (값, 인덱스) 형태
    result = [-1 for _ in range(len(numbers))]
    
    for i, num in enumerate(numbers):
        while stack and num > stack[-1][0]:
            _, index = stack.pop()
            result[index] = num
        stack.append((num, i))
    
    return result