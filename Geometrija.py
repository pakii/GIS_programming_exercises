import math as m
class Tacka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pomeriZa(self, x_pomeraj, y_pomeraj):
        self.x += x_pomeraj
        self.y += y_pomeraj

    def rastojanjeDo(self, t):
        return m.sqrt((self.x - t.x) ** 2 + (self.y - t.y) ** 2)

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


class Duz:
    def __init__(self, poc, kraj):
        self.poc = poc
        self.kraj = kraj

    @classmethod
    def duzKoor(cls, xp, yp, xk, yk):
        p = Tacka(xp, yp)
        k = Tacka(xk, yk)
        return cls(p, k)

    @property
    def duzina(self):
        return self.poc.rastojanjeDo(self.kraj)

    def __str__(self):
        return '\npocetna tacka: ' + str(self.poc) + '\nkrajnja tacka: ' + str(self.kraj)\
    + '\nduzina: ' + str(self.duzina)
