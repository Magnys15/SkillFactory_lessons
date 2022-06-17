# Напишите программу, которая на вход принимает последовательность целых чисел, и
# возвращает True, если все числа ненулевые, и False, если хотя бы одно число равно 0.

# L = list(map(int, input().split()))
# print(all(L))
# print(any(L))


# N = input()
# print(N)
# print(type(N))
#
# N = input().split()
# print(N)
# print(type(N))
#
# N = list(input().split())
# print(N)
# print(type(N))
#
# N = map(int, input().split())
# print(N)
# print(type(N))
#
# N = list(map(int, input().split()))
# print(N)
# print(type(N))
#

# N = list(map(int, input().split()))
# print(not any(N))

squares = [(i, i**2, "*" * i) for i in range(1, 11)]
print(squares)