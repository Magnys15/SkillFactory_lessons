a = int(input())

if type(a) == int:
    print("Число целое")
if 100 <= a <= 999:
    print("Числов в промежутке")
if a % 2 == 0:
    print("Число", a, "четное",)
if a % 2 == 0 and a % 3 == 0:
    print("Число делится на 2 и 3")


if type(a) == int:
    if 100 <= a <= 999:
        if a % 2 == 0:
            if a % 3 == 0:
                print("OK")

if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
    print("Число удовлетворяет условиям")

if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Число удовлетворяет условиям")