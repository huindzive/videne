n = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        n += 1
        print('ledusskapis')
    elif i % 3 == 0:
        print('ledus')
    elif i % 5 == 0:
        print('skapis')
    else:
        print(i)


