def solution(files):
    new_file_list = [] # [(ORIG, HEAD, NUMBER, ORDER), ...]
    for order, file in enumerate(files): # "foo9.txt"
        char_list = list(file) # ["f", "o", "o", "9", ".", "t", "x", "t"]
        
        head = ""
        number = ""
        status = 0 # 0 : HEAD, 1: NUMBER
        for i, char in enumerate(char_list):
            if "0" <= char and char <= "9":
                if status == 0:
                    status = 1
                number += char

            elif status == 0: # 문자입력, HEAD 입력중
                head += char
                
            elif status == 1: # NUMBER 입력 종료
                break
        head = head.lower() # 대소문자 미구분
        number = int(number) # 숫자로 변환
            
        new_file_list.append((file, head, number, order))

    new_file_list.sort(key=lambda x:[x[1], x[2], x[3]])
    
    return [x[0] for x in new_file_list]