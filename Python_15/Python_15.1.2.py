# # f = open('Test_text.txt', 'w')
# myFile = open('Test_text.txt', 'w', encoding='utf8')
#
# # Одинаковые действия для записи в файл
# myFile.write("RRRRRRR")
# print('FFFFFFFF', file=myFile)


with open("Python_15.1.5/Test_text.txt", encoding='utf8') as myFile:
    for line in myFile:
        print(line)

f = open("Python_15.1.5/Test_text.txt", encoding='utf8')
data = f.read()
numer_of_characters = len(data)
print(numer_of_characters)