class laiks:
    def __init__(self,min,sek):
        self.min = min
        if sek < 1 or sek > 59:
            self.sek = 1
            print('sekundes nav pareizas')
        else:
            self.sek = sek

    def nextsek(self):
        if self.sek < 59:
            self.sek += 1
        else:
            self.sek = 0
            self.min += 1
    
    def printlaiks(self):
        print(str(self.min) + ' ' + str(self.sek))

lai = laiks(3,58)
lai.printlaiks()
lai.nextsek()
lai.printlaiks()
lai.nextsek()
lai.printlaiks()
lai.nextsek()
lai.printlaiks()
lai.nextsek()