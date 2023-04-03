class todolist:
    def __init__(self,darbi):
        self.d = darbi

    def darbs(self):
        if self.d > 0:
            self.d = self.d -  1
            return 'vel jādara'

        elif self.d == 0:
            return 'all done'

ss = todolist(1)
print(ss.darbs())
print(ss.darbs())