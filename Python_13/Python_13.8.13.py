T = [[int(input()) % 2 == 0 for j in range(0, 2)] for i in range(0, 2)]
print(T)
print(any(T) and all(T))


