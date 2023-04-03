#for i in range(10):
#    for j in range(10):
 #       print(i,j,end='   ')
  #  print()

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

# print(a[1][1]) * lai izvadītu noteiktu skaitli

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='  ')
    print()

for j in range(len(a[1])):
    print(a[1][j], end=' ') #noteikta rinda
print()

for i in range(len(a)):
    print(a[1][j], end=' ') #noteikta kolonna(stabiņš)
print()

