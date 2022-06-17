# Реализуйте программу, которая сжимает последовательность символов.
# На вход подается последовательность вида: aaabbccccdaa
# Необходимо вывести строку, состоящую из символов и количества
# повторений этого символа. Вывод должен выглядеть как: a3b2c4d1a2


N = "aaabbccccdaa"
print(N)

first = N[0]
num = 0

result = ''

for i in N:
    if first == i:
        num = num + 1
    else:
        result = result + first + str(num)
        first = i
        num = 1

result = result + first + str(num)
print(result)


