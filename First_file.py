
# print("Hello World")

# ______________________________________________________________

# x = int(input())
# mass = []
#
# for i in range(x):
#     mass.append(list(map(int, input().split())))
# print(mass)



#
#
# x = 3

#
# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
#
#
# func()
# print(x)
#
# # Вызов функции через функцию
# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
#
# hello_world_func = get_my_func()  # получить функцию в качестве результата
#
# print(type(hello_world_func))  # <class 'function'>
# hello_world_func()





# def my_animal_generator():
#     yield "cow"
#     print('---')
#     for animal in ['cat', 'dog', 'parrot']:
#         yield animal
#     print('---')
#     print('god')
#
#
# ite = my_animal_generator()
#
# for i in ite:
#     print(i)
#
# lt = ['sdf', '123', 'haha', 'asddddd']


# ______________________________________________________________
# text = input().split()
#
# def mostLenght(text):
#     most_lenght = []
#     qty_most_lenght = 0
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for item in text:
#         word_chars = []
#         for char in item:
#
#             if char not in alphabet:
#                 word_chars.append(False)
#             else:
#                 word_chars.append(True)
#
#             if char in word_chars is False:
#                 charEn = False
#
#                 if charEn:
#                     qty = len(item)
#                     if qty > qty_most_lenght:
#                         qty_most_lenght = qty
#                         most_lenght = [item]
#                     elif qty == qty_most_lenght:
#                         most_lenght.append(item)
#
#     return list(set(most_lenght))
#
# print(mostLenght(text))


# ______________________________________________________________



class FootballClub:
    pass

Ivanov = FootballClub()
print(type(Ivanov))
Ivanov.name = 'Ivanov'
print(Ivanov.name)


fff = [1, 2, 3, 4, 5]

print(fff[4])