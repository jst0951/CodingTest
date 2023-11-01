def solution(prices):
    result_list = [0 for _ in range(len(prices))]
    
    old_stack = [] # [값, idx]
    for i in range(len(prices)):
        price = prices[i]
        
        old_stack.sort(key = lambda x:-x[0])
        while old_stack:
            old_price, old_idx = old_stack[0]
            # 가격이 떨어진 경우
            if old_price > price:
                # result_list 확정
                result_list[old_idx] = i - old_idx
                # stack에서 제거
                old_stack.pop(0)
            else:
                break
        
        # 스택에 추가
        old_stack.append([price, i])
    
    for old in old_stack:
        old_price, old_idx = old
        result_list[old_idx] = len(prices) - old_idx - 1
    
    return result_list