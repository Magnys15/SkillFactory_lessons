# Нахождение фаториала числа (простейший приемр рекурсии)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# Задание 14.2.3
# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
def summ(n):
    if n == 1:
        return 1

    return n + summ(n - 1)


print(summ(5))

