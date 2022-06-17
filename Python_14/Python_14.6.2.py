def even_number(x):
    if x % 2 == 0:
        return x


result = filter(even_number, [-2, -1, 0, 2, 4, 6, 9, 11])

print(list(result))


#Чаще всего генераторы списков более читаемы, чем map и filter, особенно в простых конструкциях.
some_list = [i - 10 for i in range(20)]
def pow2(x): return x**2
def positive(x): return x > 0

print(some_list)
print(list(map(pow2, filter(positive, some_list))))

# Тоже самое через list comprehension.
res = [i**2 for i in some_list if i > 0]
print(res)

#Возникает вопрос, когда использовать map, а когда list comprehension?
# Как оговаривалось ранее, map работает по принципу ленивых вычислений,
# а list comprehension возвращает результат вычислений сразу.

