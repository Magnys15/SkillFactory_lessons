import googletrans
print(googletrans.LANGUAGES)
from googletrans import Translator


with open("en_text.html", encoding='utf8') as flow:
    strfile = flow.readlines()

print(strfile[0])


def split_text(text):
    for char in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~--.':
        text = text.replace(char, "")

    return text.split()

list_fin =[]
for string in strfile:
    list = split_text(string)


    for word_i in range(len(list)):

        if 'quot' in list[word_i]:

            word = list[word_i].replace('quot', '')
            list[word_i] = word

    j_list = ' '.join(list)
    list_fin.append(j_list)

    print(list)
    print(' '.join(list))

print()
print(list_fin)

for sentence in list_fin:
    print(sentence, end='\n')


translator = Translator()
for sentence_i in range(len(list_fin)):
    trans_result = translator.translate(list_fin[sentence_i], dest='ru')
    trans_result = '\t\t\t&quot;' + trans_result.text + '&quot;,'
    list_fin[sentence_i] = trans_result
print(list_fin)


with open('clear_en_text.txt', 'w', encoding='utf8') as myfile:
    for sentence in list_fin:
        myfile.write(sentence + '\n')






