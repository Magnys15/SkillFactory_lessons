try:
    x = input()
    x = int(x)
except ValueError as v:
    print("не вышло конвертировать в числа")
    print(v)

else:
    print("Вы ввели", x)

finally:
    print("Выход из программы")


try:
    i = int(input('Введите число:\t'))
except ValueError as e:
    print('Вы ввели неправильное число')
    print(e)
else:
    print(f'Вы ввели {i}')
finally:
    print('Выход из программы')
