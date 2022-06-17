str_ = "my tst"
str_iter = iter(str_)

print(type(str_))  # строка
print(type(str_iter))  # итератор строки


print(str_)
print(str_iter)


print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))

# print(next(str_iter))

def first_gen(input_):
    yield input_

    input_ += 1
    print(input_)


my_first_gen = first_gen(5)

print(next(my_first_gen))
print(next(my_first_gen))
