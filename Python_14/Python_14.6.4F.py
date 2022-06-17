# f = open('Test_text.txt', 'w')
file = open('Test_text.txt', encoding='utf8')



n = 0
for line in file:
    n = n + 1
    print(line)

print(n)

