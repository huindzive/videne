from turtle import *
from random import *
penup()
goto(-140,140)
for solis in range(15):
  write(solis, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
ada=Turtle()
ada.color('blue')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()
  
bob=Turtle()
bob.color('green')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()

coc=Turtle()
coc.color('brown')
coc.shape('turtle')

coc.penup()
coc.goto(-160,40)
coc.pendown()

dad=Turtle()
dad.color('grey')
dad.shape('turtle')

dad.penup()
dad.goto(-160,10)
dad.pendown()

for gajiens in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  coc.forward(randint(1,5))
  dad.forward(randint(1,5))