#sazarojumi
#1.uzd.
sezona=input("Ievadi sezonu")
if sezona=="vasara":
    print("Grietiņa brauc ar riteni")
else:
    print("Grietiņa brauc ar slēpēm")
#2.uzd. 
s=float(input('ievadiet pirkumu summu'))
if s>=400 and s<=500:
    print(s*0.9)
elif s>500:
    print(s*0.85)
else:
    print(s)
    
#3.uzd.
import random
Lietotājs=int(input("Ievadi slaitli no 1 līdz 3"))
Dators=random.randint(1,3)
if Lietotājs==Dators:
    print("Lietotājs uzvarēja!")
else:
    print("Dators uzvarēja!")
    
#4.uzd.
import random
a=random.randint(1,100)
sk=int(input("ievadi skaitli no 1 līdz 100"))
if sk>a:
    print("Tu uzvarēji")
elif sk<a:
    print("Tu zaudēji")
else :
    print("neizšķirts")


#CIKLS FOR
#1.uzdevums
summa=0 #tiek definēts mainīgais pirms cikla
for i in range(10): #cikls for darbosies 10 reizes
    skaitlis=float(input('Ievadi skaitli')) #liek lietotājam ievadīt reālu skaitli
    summa=summa+skaitlis #mainīgajam summa tiek pieskaitīts ievadītais skaitlis
print(summa/10) #tiek izvadīts 10 skaitļu vidējais

#2.uzdevums
summa=0
for i in range(5,1001,5): #pirmais skaitlis, kas dalās ar 5 intervālā ir 5, nākamais ir 10,
#tādēļ solis 5
    summa=summa+i #i ir tas kas mainās un tiek pieskaitīts summai
    print(summa)

#3.uzdevums
sk=int(input('Ievadi skaitli kam tiks rēķināts faktoriāls'))
faktoriāls =1 #mainīgais tiek definēts pirms cikla un tas ir 1, lai galarezultātā nebūtu 0
for i in range(1,sk+1): #plus viens tādēļ, lai tiktu iekļauts galapunkts
    faktoriāls=faktoriāls*i #i ir tas, kas mainās noteiktajā intervālā
print(faktoriāls)