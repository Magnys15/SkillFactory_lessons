# Задание 14.2.2
# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.
def multiplier(*args):
    res = 1
    for n in args:
        res = res * n

    return res


N = list(map(int, input().split()))
print(N)
print(multiplier(*N))

