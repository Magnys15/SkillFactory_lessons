a = int(input())
b = int(input())
c = int(input())

if (a < 45) and (b >= 45) and (c >= 45)  \
    or (a >= 45) and (b >= 45) and (c < 45) \
    or (a >= 45) and (b < 45) and (c >= 45):
    print("есть 1 чило < 45")
else:
    print(" Нет числа < 45 или их несколько")

