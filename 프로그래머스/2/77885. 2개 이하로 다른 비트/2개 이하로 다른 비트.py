def solution(numbers):
    result = []
    for number in numbers:
        binary = '0' + bin(number)[2:]
        # '0'으로 끝나는 경우
        if binary.endswith('0'):
            f_x = int(binary[:-1] + '1', 2)
        # '1'으로 끝나는 경우
        elif binary.endswith('1'):
            # 맨 뒤의 '0' 찾기
            for i in range(len(binary)-1, -1, -1):
                if binary[i] == '0':
                    # '1'로 바꾸기
                    binary = binary[:i] + '1' + binary[i+1:]
                    break
            # 바꾼것이 맨 위 수인 경우(즉, 7과 같이 꽉 차있던 경우)
            if binary.startswith('1'):
                # 맨 윗 수 제외 가장 먼저 나오는 '1'을 '0'으로
                for i in range(1, len(binary)):
                    if binary[i] == '1':
                        binary = binary[:i] + '0' + binary[i+1:]
                        break
            # 아닌 경우, 최대한 줄이기 위해 그 바로 뒷 수 '0'으로 하기
            else:
                binary = binary[:i+1] + '0' + binary[i+2:]
            f_x = int(binary, 2)
        result.append(f_x)
    return result