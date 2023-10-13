def solution(numbers):
    result = ''
    
    number_list = [list(str(number)) for number in numbers]
    number_list.sort(key=lambda x:(x * 4)[:4], reverse = True)
    for number in number_list:
        result += ''.join(number)
    
    if '0' in result and len(result) == result.count('0'):
        return '0'
    return result