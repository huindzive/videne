# programma, kas ievadītam cetrciparu skaitlim samaina vietam divus videjos
x = int(input('ievadi cetrciparu skaitli! '))  # 1234
if 1000 <= x <= 9999:
    ceturtais = x % 10 # ceturtais = 4
    tresais = (x % 100 - ceturtais)/10 # 34 -> 30 -> 3
    otrais = (x % 1000 - tresais * 10 - ceturtais)/100 # 234 -> 204 -> 200 -> 2
    pirmais = (x - otrais * 100 - tresais * 10 - ceturtais)/1000 # 1234 -> 1034 -> 1004 -> 4 -> 1
    skaitlis = int(pirmais * 1000 + tresais * 100 + otrais * 10 + ceturtais)
    print(skaitlis)
