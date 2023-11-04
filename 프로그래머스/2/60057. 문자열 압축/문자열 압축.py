from collections import deque

def solution(s):
    compressed_str_list = []
    
    for i in range(1, len(s) + 1):
        # i만큼 문자를 잘라 압축
        
        # 압축 전 문자열 잘라 담기
        before_list = []
        cut_cnt = int(len(s) / i)
        for cut_idx in range(cut_cnt):
            before_list.append(s[i*cut_idx : i*(cut_idx+1)])
        # 자른 후 남은 문자열 집어넣기
        if len(s) % i > 0:
            before_list.append(s[i*(cut_idx+1):])
        
        # 압축
        queue = deque(before_list)
        count = 0
        ex_cut_str = ''
        compressed_str = ''
        while queue:
            cut_str = queue.popleft()
            if cut_str == ex_cut_str:
                count += 1
            else:
                # 과거 반복중이던 문자열 압축 완료(결과에 추가)
                if count == 0 or count == 1:
                    compressed_str += ex_cut_str
                else:
                    compressed_str += (str(count) + ex_cut_str)
                # 이제 해당 문자열이 새로운 검증 대상
                ex_cut_str = cut_str
                count = 1
            
        # 마지막 압축 문자열 처리
        if count == 0 or count == 1:
            compressed_str += ex_cut_str
        else:
            compressed_str += (str(count) + ex_cut_str)
        compressed_str_list.append(compressed_str)

    length_list = [len(s) for s in compressed_str_list]
    return min(length_list)