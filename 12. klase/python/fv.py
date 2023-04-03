import math as m

class point:
    def __init__(self,X,Y):
        self.x = X
        self.y = Y

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def getXY(self):
        return [self.x,self.y]

    def distanceTo(self,point):
        dx = self.x - point.x
        dy = self.y - point.y
        return (dx**2 + dy**2) ** 0.5

# p1 = point(4,7)
# p2 = point(5,10)
# print(p1.getXY())
# print(p1.distanceTo(p2))
def isTaisnlenka(a,b,c):
    if a  == m.sqrt(b**2 + c **2) or b  == m.sqrt(a**2 + c **2) or c == m.sqrt(b**2 + a **2):
        return True
    else:
        return False
    


class triangle:
    def __init__(self,point1,point2,point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def perimeter(self):
        mala1 = self.point1.distanceTo(self.point2)
        mala2 = self.point1.distanceTo(self.point3)
        mala3 = self.point3.distanceTo(self.point2)
        return mala1 + mala2 + mala3 

    def surface(self):
        mala1 = self.point1.distanceTo(self.point2)
        mala2 = self.point1.distanceTo(self.point3)
        mala3 = self.point3.distanceTo(self.point2)
        p = self.perimeter()/2
        s = (p*(p-mala1)*(p-mala2)*(p-mala3)) **0.5
        return s

    def getType(self):
        mala1 = self.point1.distanceTo(self.point2)
        mala2 = self.point1.distanceTo(self.point3)
        mala3 = self.point3.distanceTo(self.point2)
        if mala1 == mala2 == mala3 :
            return 'regulārs'
        elif mala1 == mala2 or mala2 == mala3 or mala1 == mala3:
            if isTaisnlenka(mala1,mala2,mala3):
                return 'taisnlenķa vienādsānu'
            else:    
                return 'vienādsānu'
        else:
            if isTaisnlenka(mala1,mala2,mala3):
                return'taisnleķa dažādmalu'
            else:
                return 'dažādmalu'



t1 = point(0,0)
t2 = point(3,0)
t3 = point(3,3)

tri = triangle(t1,t2,t3)
print(tri.perimeter())
print(tri.surface())
print(tri.getType())



