from Python_Rec import Rectangle, Square, Circle
from Python_Rec import Cat

r1 = Rectangle(2, 4)
r2 = Rectangle(4, 6)
print(r1.getArea())
print(r2.getArea())
print()

print("Rectangle", r1.parameters())
print()

s1 = Square(4)
s2 = Square(6)
print(s1.getArea())
print(s2.getArea())
print()

c1 = Circle(2)
c2 = Circle(5)
print(c1.getArea())
print(c2.getArea())
print()

figures = [r1, s1, r2, s2, c1, c2]
print()

for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.getArea(), 'Прямоугольник')
    elif isinstance(figure, Circle):
        print(figure.getArea(), 'Круг')
    else:
        print(figure.getArea(), 'Квадрат')

print('_____________________')

cats_list = []
Gogen = Cat('Gogen', 'Мальчик', 2)
cats_list.append(Gogen)

print('Начальный список', cats_list)

for i in range(2):
    # new_cat = Cat(input(),input(),input())             Аналогично строке 48


    cats_list.append(Cat(input(),input(),input()))

print()

n = 0
for cat in cats_list:
    n += 1
    print(f'{n} кот:')
    for at in reversed(dir(cat)):
        if not at.startswith('_'):
            print(getattr(cat, at))
    print()

print('Конечный список', cats_list)
print()

print("___________________________")

for cat in range(len(cats_list)):
    print(cats_list[cat].name)
    print(cats_list[cat].gender)
    print(cats_list[cat].age)
    print()

print("____________________________")





