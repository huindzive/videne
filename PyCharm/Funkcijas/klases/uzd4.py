#klase checklist
class Checklist:
    def __init__(self,skaits):
        self.skaits = skaits
    def Check(self):
        if self.skaits > 0:
            self. skaits -= 1
            if self.skaits == 0:
                print('all done')
            else:
                print(self.skaits, 'tasks left' )
    def AddTask(self):
        self.skaits += 1
        print(self.skaits, 'tasks left')


list = Checklist(5)
list.Check()
list.AddTask()
list.Check()
list.Check()
list.Check()
list.Check()
list.Check()
