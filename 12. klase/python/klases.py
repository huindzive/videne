class Circle:
    def __init__(self,radiuss,color='white'):
        self.radiuss = radiuss
        self.color = color

    def getRadiuss(self):
        return self.radiuss

    def setRadiuss(self,r):
        self.radiuss = r

    def getArea(self):
        return self.radiuss ** 2 * 3.14159265

    def getCircumference(self):
        return 2 * self.radiuss *  3.14159265

    def toString(self):
        return str(self.getRadiuss()) + ' ' + str(self.getCircumference()) + ' ' + str(self.getArea)

circle1 = Circle(5,'red')
print(circle1.getRadiuss())
print(circle1.getCircumference())
print(circle1.getArea())


class employee:
    def __init__(self,ID,firstName,lastName,salary):
        self.id = ID
        self.name = firstName
        self.surname = lastName
        self.salary = salary

    def getName(self):
        # self.fullname = fullname
        return self.name + ' ' + self.surname

    def getAnnualSalary(self):
        return self.salary * 12

    def raiseSalary(self,raised):
        self.raised = raised
        self.salary = self.salary * (1 + (self.raised/100))
        return self.salary

john = employee(15,'John','Deere',1400)
print(john.getName())
print(john.getAnnualSalary())
john.raiseSalary(10)
print(john.getAnnualSalary())


class InvoiceItem:
    def __init__(self,name,price,qty = 1):
        self.name = name
        self.price = price
        self.qty = qty

    def setQty(self,qty):
        self.qty = qty
        
    def getTotal(self):
        return round(self.price * self.qty,2)

    def toString(self):
        return str(self.qty) + ' ' + str(self.name) + 'costs $  ' + str(self.getTotal())

apple = InvoiceItem('apple',0.23)
apple.setQty(5)
print(apple.toString())



class bankAccount:
    def __init__(self, ID, Name, Balance = 0):
        self.id = ID
        self.name = Name
        self.balance = Balance

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    def credit(self,amount):
        self.balance += amount

    def transferTo(self,account,amount):
        if amount <= self.getBalance() and self.getID() != account.getID() :
            self.balance -= amount
            account.credit(amount)

        else:
            print('account',self.getID(), "has insufficient funds and/or it's the same account", sep=" ")

account1 = bankAccount(21,'Arturs Balnass',130)
account2 = bankAccount(51,'Jānis Kriervinjsh',500)

print(account1.getBalance())
print(account2.getBalance())

account1.transferTo(account2,120)

print(account1.getBalance())
print(account2.getBalance())

account1.transferTo(account2,120)



def isLeapYear(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

def formatDate(d):
    if d < 10:
        return '0' + str(d)
    else:
        return str(d)

class Date:
    def __init__(self ,d,m,y):
        if [4,6,9,11].count(m):
            if d > 0 and d < 31:
                self.d = d
                self.m = m
                self.y = y

            else:
                print('invalid imput')
                self.d = 1
                self.m = m
                self.y = y
        elif m == 2:
            if isLeapYear(y) and d> 0 and d<30:
                self.d = d
                self.m = m
                self.y = y
            elif (not isLeapYear(y)) and d> 0 and d<29:
                self.d = d
                self.m = m
                self.y = y
            else:
                print('invalid imput')
                self.d = 1
                self.m = m
                self.y = y
        else:
            if d> 0 and d < 32 and [1,3,5,7,8,10,12].count(m):
                self.d = d
                self.m = m
                self.y = y
            else:
                print('invalid imput')
                self.d = 1
                self.m = m
                self.y = y
    def toString(self):
        return formatDate(self.d) + '/' + formatDate(self.m) + '/' + str(self.y)



dzD = Date(29,2,2012)

print(dzD.toString())

def formatDate(d):
    if d < 10:
        return '0' + str(d)
    else:
        return str(d)

class time:
    def __init__(self,h,m,s):
        if s < 60 and s >= 0:
            if m >= 0 and m < 60:
                if h >= 0 and h < 24:
                    self.s = s
                    self.m = m
                    self.h = h
                else:
                    print('invalid timestamp')
                    self.s = 0
                    self.m = 0
                    self.h = 0

            else:
                print('invalid timestamp')
                self.s = 0
                self.m = 0
                self.h = 0

        else:
            print('invalid timestamp')
            self.s = 0
            self.m = 0
            self.h = 0

    def toString(self):
        return formatDate(self.h) + ':' + formatDate(self.m) + ':' + formatDate(self.s)

    def addTime(self,time):
        print(self.toString() , time.toString())
        seconds = self.s + time.s
        minutes = self.m + time.m
        hours = self.h + time.h

        print(minutes)

        if seconds > 59:
            minutes += 1
            seconds = seconds % 60
        if minutes > 59:
            hours += 1
            minutes = minutes % 60
        if hours > 23:
            hours = hours % 24


        self.s = seconds
        self.m = minutes
        self.h = hours

n = time(0,45,16)
m = time(2,18,54)

n.addTime(m)
print(n.toString())
