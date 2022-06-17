import re


def split_text(text):
    for char in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~--.':
        text = text.replace(char, "")

    return text.split()

# def longest_word(list_text):
#     count = 0
#     for word_i in range(len(list_text) + 1):
#         for word_j in range(len(list_text)):
#             if list_text[word_i] == list_text[word_j]:
#                 count += 1
#                 print(list_text[word_i], count)
#                 print('---')
#             print('--')
#         print('-')


def longest_en_word(list_text):
    word_length = 0
    words = []
    charEn = None
    alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for word_i in list_text:
        for char in word_i:
            if char not in alfa:
                charEn = False
            else:
                charEn = True

        if charEn:
            if word_length < len(word_i):
                word_length = len(word_i)
                words = [word_i]
            elif word_length == len(word_i):
                words.append(word_i)
    return f"Самое длинное слово: {words}. Его длина {word_length} символов"


def most_common(list_text, length=0):
    common_word_num = 0
    common_words = []
    for word_i in list_text:
        if len(word_i) > length:
            if common_word_num < list_text.count(word_i):
                common_word_num = list_text.count(word_i)
                common_words = [word_i]
            elif common_word_num == list_text.count(word_i) and word_i not in common_words:
                common_words.append(word_i)
    return f"Слово/а {common_words} встретились {common_word_num} раз/а"


myFile = open("Text_file.txt", 'r', encoding="utf8")
strfile = myFile.read()


print(strfile)
print()

st = split_text(strfile)
print(st)
print()

lew = longest_en_word(st)
print('___')
mc = most_common(st, 3)


with open("output.txt", 'w', encoding="utf8") as myFile:
    myFile.write(lew)
    myFile.write("\n")
    myFile.write(mc)









