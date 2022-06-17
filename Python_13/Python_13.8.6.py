# Задание 13.8.6
a = 2
b = None

if a and b is not None:
    print(a == b)

a = b if a and b is not None else a != b

print(a)



