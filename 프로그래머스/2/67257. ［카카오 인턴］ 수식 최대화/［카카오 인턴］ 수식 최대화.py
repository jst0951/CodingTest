from itertools import permutations

def solution(expression):
    num_list = []
    op_list = []
    start_idx = 0
    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*']:
            # operation 등록
            op_list.append(expression[i])
            # 전에 숫자가 있던 경우, 추가
            num_list.append(int(expression[start_idx:i]))
            # 시작 idx 갱신
            start_idx = i + 1
    # 마지막 수 저장
    num_list.append(int(expression[start_idx:]))
    
    # 우선연산 순위 지정
    priority_list = list(permutations(['+', '-', '*'], 3))
    
    result_list = [] # 연산 결과 리스트
    for priority in priority_list:
        # 원본 복제
        _num_list = num_list[:]
        _op_list = op_list[:]
        for most_prior in priority:
            while most_prior in _op_list:
                idx = _op_list.index(most_prior)
                _op_list.pop(idx)
                a = _num_list.pop(idx)
                b = _num_list.pop(idx)
                if most_prior == '+':
                    res = a + b
                elif most_prior == '-':
                    res = a - b
                elif most_prior == '*':
                    res = a * b
                # _num_list에 결과 등록
                _num_list.insert(idx, res)
        result_list.append(abs(_num_list[0]))
    return max(result_list)