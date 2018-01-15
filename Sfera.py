import math as m


class Sfera:
    brojObjekata = 0

    def __init__(self, poluprecnik=1, xCentar=0, yCentar=0, zCentar=0):
        self.poluprecnik = poluprecnik
        self.xCentar = xCentar
        self.yCentar = yCentar
        self.zCentar = zCentar
        Sfera.brojObjekata += 1

    @property
    def izracunajZapreminu(self):
        return 4 * m.pi * self.poluprecnik ** 3 / 3.0

    @staticmethod
    def ukupanBrojKreiranihObjekata():
        print 'Broj formiranih objekata: ' + str(Sfera.brojObjekata)
