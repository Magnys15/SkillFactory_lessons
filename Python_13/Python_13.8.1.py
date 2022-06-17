some_var = None
if some_var is None:
    print("NoneType")
else:
    print(type(some_var))

a = '' # пустая строка
b = a or 1
print(b)



print(False or 0 or False)
