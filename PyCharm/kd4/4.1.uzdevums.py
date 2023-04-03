n=int(input('ievadi n, kas ir lielās par 2: '))
b = []
for i in range(n):
    rin = []
    for j in range(n):
        if i == 0 or j == n-1 or j == 0 or i == n-1:
            rin.append(1)
        else:
            rin.append(0)
    b.append(rin)
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=' ')
    print()