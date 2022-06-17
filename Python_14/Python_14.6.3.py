#Предположим у нас есть список с данными о росте и весе людей.
# Задача — отсортировать их по индексу массы тела. Он вычисляется
# по формуле: свой рост в метрах возвести в квадрат, потом массу тела
# в килограммах разделить на полученную цифру.

data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]


a = sorted(data, key = lambda x: x[0]/x[1]**2)

print(a)

print(min(data, key=lambda x: x[0] / x[1] ** 2))  # отбор по ключу


a = ["asd", "bbd", "ddfa", "mcsa"]

print(list(map(len, a)))
print(list(map(str.upper, a)))
