import numpy

# N = int(input("Ведите количество строк"))
# M = int(input("Ведите количество столбцов"))
#
# mass = int[N,M]
#
# for i in range(N):
#     for j in range(M):
#       mass[N][M] = int(input())
#
#     # mass.append(int(input('Введите %d число' )))




n = int(input("Ведите количество строк"))
m = int(input("Ведите количество столбцов"))

mass = [[0 for i in range(n)] for j in range(m)]
# mass = numpy.empty((n, m))

for i in range(n):
    for j in range(m):
        mass[i][j] = int(input())

for i in range(n):
    for j in range(m):
        print(mass[i][j], end=' ')
    print()

mass_MAX = mass[0][0]
mass_MIN = mass[0][0]
for i in range(n):
    mass_max_row = mass[i][0]
    mass_min_row = mass[i][0]
    for j in range(m):
        if mass[i][j] > mass_max_row:
            mass_max_row = mass[i][j]
        if mass[i][j] < mass_min_row:
            mass_min_row = mass[i][j]

        if mass_max_row > mass_MAX:
            mass_MAX = mass_max_row
        if mass_min_row < mass_MIN:
            mass_MIN = mass_min_row

    print(mass_max_row, "max_row")
    print(mass_min_row, "min_row")

print()
print(mass_MAX, "max")
print(mass_MIN, "min")



for i, value in enumerate(mass):
    print("Значение элемента: ", value)
    for j, value_2 in enumerate(value):
        print("Индекс элемента: ", i, j)
        print("Значение элемента: ", value_2)  # с помощью индекса получаем значение элемента
        print("--")
print("Конец цикла")
