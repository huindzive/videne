a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# kollonu ciparu summa
print()

for i in range(len(a)):
    sum = 0
    for j in range(len(a[i])):
        sum += a[j][i]
    print(sum, end=' ')
