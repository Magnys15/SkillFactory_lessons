# Напишите функцию, которая будет возвращать количество делителей числа а.

def number_of_divisors(n):
    counter = 0
    c = 1
    for i in range(1, n+1):
        if n % c == 0:
            counter = counter + 1
        c = c + 1
    return counter


A = int(input())
print(number_of_divisors(A))

