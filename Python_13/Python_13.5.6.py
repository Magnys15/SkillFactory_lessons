# Запишите логическое выражение, которое определяет, что число А не принадлежит
# интервалу от -10 до -1 или интервалу от 2 до 15.
x = int(input())

if not (-10 <= x <= -1) or (2 <= x <= 15):
    print('-')
else:
    print("+")