
#1.uzd.
sezona=input(&quot;Ievadi sezonu&quot;)
if sezona==&quot;vasara&quot;:
    print(&quot;Grietiņa brauc ar riteni&quot;)
else:
    print(&quot;Grietiņa brauc ar slēpēm&quot;)
#2.uzd. 
s=float(input(&#039;ievadiet pirkumu summu&#039;))
if s&gt;=400 and s&lt;=500:
    print(s*0.9)
elif s&gt;500:
    print(s*0.85)
else:
    print(s)
    
#3.uzd.
import random
Lietotājs=int(input(&quot;Ievadi slaitli no 1 līdz 3&quot;))
Dators=random.randint(1,3)
if Lietotājs==Dators:
    print(&quot;Lietotājs uzvarēja!&quot;)
else:
    print(&quot;Dators uzvarēja!&quot;)
    
#4.uzd.
import random
a=random.randint(1,100)
sk=int(input(&quot;ievadi skaitli no 1 līdz 100&quot;))
if sk&gt;a:
    print(&quot;Tu uzvarēji&quot;)
elif sk&lt;a:
    print(&quot;Tu zaudēji&quot;)
else :
    print(&quot;neiz&scaron;ķirts&quot;)


#CIKLS FOR
#1.uzdevums
summa=0 #tiek definēts mainīgais pirms cikla
for i in range(10): #cikls for darbosies 10 reizes
    skaitlis=float(input(&#039;Ievadi skaitli&#039;)) #liek lietotājam ievadīt reālu skaitli
    summa=summa+skaitlis #mainīgajam summa tiek pieskaitīts ievadītais skaitlis
print(summa/10) #tiek izvadīts 10 skaitļu vidējais

#2.uzdevums
summa=0
for i in range(5,1001,5): #pirmais skaitlis, kas dalās ar 5 intervālā ir 5, nākamais ir 10,
#tādēļ solis 5
    summa=summa+i #i ir tas kas mainās un tiek pieskaitīts summai
    print(summa)

#3.uzdevums
sk=int(input(&#039;Ievadi skaitli kam tiks rēķināts faktoriāls&#039;))
faktoriāls =1 #mainīgais tiek definēts pirms cikla un tas ir 1, lai galarezultātā nebūtu 0
for i in range(1,sk+1): #plus viens tādēļ, lai tiktu iekļauts galapunkts
    faktoriāls=faktoriāls*i #i ir tas, kas mainās noteiktajā intervālā
print(faktoriāls)</div></pre>