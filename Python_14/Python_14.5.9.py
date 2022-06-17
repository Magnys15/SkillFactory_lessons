
# Рекурсия по поиску минимального значения в списке
def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])


L = [2,4,7,2,34,7,4,0.4,4,5,]


M = min_list(L)
print(M)

