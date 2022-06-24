# Сортировка выбором
print("Сортировка выбором")
array = [2, 3, 1, 4, 6, 5, 9, 8, 7, 12, 10, 11]
count = 0

for i in range(len(array)):
    i_min = i
    for j in range(i, len(array)):
        count += 1
        if array[j] < array[i_min]:
            i_min = j
    if i != i_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[i_min] = array[i_min], array[i]

print(array)
print(count, 'Итераций')
print()


# Сортировка пузырьком
print("Сортировка пузырьком")
array = [2, 3, 1, 4, 6, 5, 9, 8, 7, 12, 10, 11]
count = 0

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        count += 1
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
print(count, 'Итераций')
print()


# Сортировка вставками
print("Сортировка вставками")
array = [2, 3, 1, 4, 6, 5, 9, 8, 7, 12, 10, 11]
count = 0

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        count += 1
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x

print(array)
print(count, 'Итераций')
print()


# Сортировка слиянием
print("Сортировка слиянием")
array = [2, 3, 1, 4, 6, 5, 9, 8, 7, 12, 10, 11]

def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(merge_sort(array))
print()


# Быстрая сортировка
import random
print("Быстрая сортировка")
a = [2, 3, 1, 4, 6, 5, 9, 8, 7, 12, 10, 11]
count = 0


# def qsort_random(array, left, right):
#     p = random.choice(array[left:right + 1])
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort_random(array, left, j)
#     if right > i:
#         qsort_random(array, i, right)
#
# qsort_random(a,2,6)
#
# print(array)
# print(count)


def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
quicksort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)