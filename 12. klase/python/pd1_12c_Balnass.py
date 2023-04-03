import math as m
# Klase MyPoint, kas implementē sekojošo:

# konstruktors, kur tiek padots punkta x un y ++
# Funkcijas setX, setY, getXY, moveRight(d), moveLeft(d), ++
# moveUp(d), moveDown(d), distanceTo(point) ++
# Nodrošināt funkcionalitāti tā, lai punktu nebūtu iespējams
# pārvietot tālāk par 100 vienībām uz jebkuru pusi no
# _sākotnējās_ pozīcijas++
# izveidot MyPoint objektu, nodemonstrēt vismaz četru
# iekšējo funkciju darbību +++

class myPoint:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.limits = [self.y +100,self.x+100,self.y-100,self.x-100]
    
    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def getXY(self):
        return [self.x,self.y]

    def moveUp(self,d):
        if self.y + d > self.limits[0]:
            print('nevar izdarīt pārvietojumu')
        else:
            self.d = d
            self.y = self.y + self.d

    def moveDown(self,d):
        if self.y - d < self.limits[2]:
            print('nevar izdarīt pārvietojumu')
        else:
            self.d = d
            self.y = self.y - self.d

    def moveLeft(self,d):
        if self.x - d < self.limits[3]:
            print('nevar izdarīt pārvietojumu')
        else:
            self.d = d
            self.x = self.x - self.d

    def moveRight(self,d):
        if self.x + d > self.limits[1]:
            print('nevar izdarīt pārvietojumu')
        else:
            self.d = d
            self.x += self.d

    def distanceTo(self,point):
        dx = self.x - point.x
        dy = self.y - point.y
        return (dx**2 + dy**2) ** 0.5
    


# print(xxx.getXY())
# xxx.moveDown(4)
# print(xxx.getXY())
# xxx.moveLeft(120)
# print(xxx.getXY())


# Klase Circle, kas par centra punktu izmanto MyPoint klases objektu
# implementē visas funkcijas, kas raksturīgas riņķa līnijai
# konstruktorā MyPoint objekts un rādiuss
#


class circle:
    def __init__(self,r,center):
        self.r = r 
        self.center = center

    def surface(self):
        s = m.pi * self.r **2
        return s
    
    def linija(self):
        rl = self.r * 2 * m.pi
        return rl
    
    def overlapis(self,circle):
        if self.center.distanceTo(circle.center) > self.r + circle.r:
            return False
        else:
            return True

p1 = myPoint(4,2)
p2 = myPoint(7,7)

circle1 = circle(4,p1)
circle2 = circle(5,p2)

print(circle1.overlapis(circle2))


