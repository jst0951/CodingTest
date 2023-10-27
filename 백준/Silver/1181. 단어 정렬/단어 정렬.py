N = int(input())

word_list = []
for _ in range(N):
    word = input()
    word_list.append([word, len(word)])

word_list.sort(key = lambda x:[x[1], x[0]])

previous_word = ''
for word in word_list:
    if previous_word != word[0]:
        print(word[0])
        previous_word = word[0]