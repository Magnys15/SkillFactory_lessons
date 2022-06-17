a = 0
b = 1

if a and b:
    print('обе истинны')
    print(a, b)
elif a or b:
    print('Одна истинна')
    print(a or b)
elif (a and b) != 1:
    print('Обе ложные')
    print(a, b)

