# Задание 14.2.4
# С помощью рекурсивной функции разверните строку.

def reverse_str(string):
    if len(string) == 0:
        return ''
    else:
        return string[-1] + reverse_str(string[:-1])


print(reverse_str('test'))

