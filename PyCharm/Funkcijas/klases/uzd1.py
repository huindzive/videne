class Persona:
    def __init__(self, name, surname, height, age):
        self.name = name
        self.surname = surname
        self.height = height
        self.age = age

janis = Persona('Jānis', 'Kalniņš', 216, 23)
print(janis.age)
print()
class taisnsturis:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def p(self):
        return 2*(self.a + self.b)

    def s(self):
        return self.a * self.b

x = taisnsturis(5,7)
print(x.s(), ' ', x.p())
