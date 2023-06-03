"""
Чтобы попробовать функицонал используй файл test_2.txt
"""
try:
    file_name = input()

    file = open(file_name, 'r', encoding='utf-8')

    content = file.read()
    content_list = content.split()

    unqiue_words_list = set(content_list)
    max_mentions = 0
    max_mentioned_word = None

    for i in unqiue_words_list:
        mentions = 0
        for r in content_list:
            if i == r:
                mentions +=1
        if mentions > max_mentions:
            max_mentions = mentions
            max_mentioned_word = i
    print(max_mentioned_word)
except FileNotFoundError:
    print("Ошибка")