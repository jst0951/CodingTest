def isCorrect(p):
    cnt = 0
    for char in p:
        if char == '(':
            cnt += 1
        elif char == ')':
            if cnt > 0:
                cnt -= 1
            else:
                return False
    if cnt == 0:
        return True
    else:
        return False

def solution(p):
    # 1
    if len(p) == 0:
        return p
    
    # 2
    cnt_u = 0
    cnt_z = 0
    u = ''
    for char in p:
        u += char
        if char == '(':
            cnt_u += 1
        elif char == ')':
            cnt_z += 1
        if cnt_u == cnt_z:
            break
    v = p[(cnt_u + cnt_z):]
    
    # 3
    # u가 올바른 괄호 문자열인지 판별
    isC = isCorrect(u)
    if isC == True:
        # 3-1
        return u + solution(v)
    
    # 4
    temp = '('
    temp += solution(v)
    temp += ')'
    
    temp_list = list(u)[1:-1]
    for i in range(len(temp_list)):
        if temp_list[i] == '(':
            temp_list[i] = ')'
        else:
            temp_list[i] = '('
    temp += ''.join(temp_list)
    
    return temp
    
    
        

                