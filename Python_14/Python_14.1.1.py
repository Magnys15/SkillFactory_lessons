# Пример простейшей функции
def print_2_add_2():
    print(2 + 2)


print_2_add_2()

# Пример простейшей функции с двумя аргументами и вызов функции
def pow_func(base, n=2):
    res = base ** n
    print(res)


G = int(input())  # Вызов функции
c = int(input())
pow_func(G, c)
