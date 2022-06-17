# Задача. Дано целое число 123456789. Определите, входит ли в него цифра 5.
x = 123456789
print(type(x))

x = str(x)
print(type(x))

x = list(x)
print(x)

x = map(int, x)
print(type(x))
print(x)

x = list(x)
print(type(x))
print(x)

z = 5 in x
print(z)
print(type(z))

# Дано n-значное целое число N. Определите, входят ли в него цифры 3 и 7.
N = input()
print("3" and "7" in N)

v = int(input())
print(type(v))
print(5 in v)
