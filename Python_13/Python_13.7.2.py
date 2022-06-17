
N = int(input())

while True:
    if N % 2 == 0:
        N = N // 2
        print(N, 1)
    elif N % 2 != 0:
        N = (N * 3 + 1) // 2
        print(N, 2)
    if N == 1:
        print('yes')
        break

# В клетке находятся фазаны и кролики. Известно, что у них 35 голов и 94 ноги.
# Узнайте число фазанов и число кроликов.
legs = 94
heads = 35

for r in range(heads + 1):
    for ph in range(heads + 1):
        if r + ph > heads or r*4 + ph * 2 > legs:
            continue
        if(r + ph) == heads and (r*4 + ph * 2 == legs):
            print(r, "кроликов")
            print(ph, "фазанов")