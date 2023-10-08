alphabet_list = ["A", "E", "I", "O", "U"]
def solution(target_word):
    
    current_word = ''
    count = 0
    dict_list = []
    for alphabet_1 in alphabet_list:
        current_word += alphabet_1
        dict_list.append(current_word)
        for alphabet_2 in alphabet_list:
            current_word += alphabet_2
            dict_list.append(current_word)
            for alphabet_3 in alphabet_list:
                current_word += alphabet_3
                dict_list.append(current_word)
                for alphabet_4 in alphabet_list:
                    current_word += alphabet_4
                    dict_list.append(current_word)
                    for alphabet_5 in alphabet_list:
                        current_word += alphabet_5
                        dict_list.append(current_word)
                        current_word = current_word[:-1]
                    current_word = current_word[:-1]
                current_word = current_word[:-1]
            current_word = current_word[:-1]
        current_word = current_word[:-1]
    return dict_list.index(target_word) + 1