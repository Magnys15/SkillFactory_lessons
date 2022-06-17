# Задание 14.1.3
def divisor(a, n):
    if a % n == 0:
        print(f"Число {n} являтся делителем числа {a}")
    else:
        print(f"Число {n} не являтся делителем числа {a}")


A = int(input())
B = int(input())
divisor(A, B)


# Задание 14.1.3


def stair(n):
    while n != 0:
        print("*" * n)
        n = n - 1


C = int(input())
stair(C)

