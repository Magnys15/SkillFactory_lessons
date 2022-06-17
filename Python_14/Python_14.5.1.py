def D(a, b, c):
    return b**2 - 4*a*c


def ruts(d, a, b, c,):
    if d < 0:
        print('Нет вещественных корней')
    if d == 0:
        print('1 корень')
        return -b/(2*a)
    if d > 0:
        print('2 корня')
        x1 = (-b - d**0.5)/(2*a)
        x2 = (-b + d**0.5)/(2*a)
        res = []
        res.append(x1)
        res.append(x2)

        return res


print("Введи a,b,c")
L = list(map(int, input().split()))
# Представим, что у нас теперь аргументы хранятся не в виде списка, а в виде словаря.
#
# M = {'a' : 1,
#      'b' : 0,
#      'c' : -1}

D = D(*L)
print(D)

r = ruts(D, *L)
print(r)

