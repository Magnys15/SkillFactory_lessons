L = [i for i in range(10)]
M = [i for i in range(10, 0, -1)]

N = [x*z for x, z in zip(L,M)]
print(N)