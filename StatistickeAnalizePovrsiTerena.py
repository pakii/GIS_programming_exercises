import math as m
import random as r
import matplotlib.pyplot as plt


class Tacka:
    brojTacke = 0

    def __init__(self, y=0, x=0, z=0):
        Tacka.brojTacke += 1
        self.oznaka = 't' + str(Tacka.brojTacke)
        self.y = y
        self.x = x
        self.z = z

    def rastojanjeDo(self, t):
        return m.sqrt((self.x - t.x) ** 2 + (self.y - t.y) ** 2)

    def najblizaTacka(self, listaTacaka):
        tacke = [] + listaTacaka
        najblizaTacka = None
        minRastojanje = float('inf')
        for t in tacke:
            t.rastojanje = self.rastojanjeDo(t)
            if t.rastojanje < minRastojanje:
                minRastojanje = t.rastojanje
                najblizaTacka = t
        return najblizaTacka

    def interpolacijaNaPravcuIzmedju(self, t1, t2):
        d1 = self.rastojanjeDo(t1)
        d2 = self.rastojanjeDo(t2)
        faktor = (t2.z - t1.z) / (d1 + d2)
        h1 = t1.z + d1 * faktor
        h2 = t2.z - d2 * faktor

        self.z = (h1 + h2) / 2
        print 'Interpolovana visina pozicije (' + str(self.y) + ', ' + str(self.x) + ') : ' + str(self.z)

    def __str__(self):
        return self.oznaka + '(' + str(self.y) + ',' + str(self.x) + ')'


class Povrs:
    def __init__(self, analiticar, brTacaka, podrucjeY, podrucjeX, opsegVisina):
        self.brTacaka = brTacaka
        self.analiticar = analiticar
        self.tacke = self.kreirajRandomTacke(brTacaka, podrucjeY, podrucjeX, opsegVisina)

    def kreirajRandomTacke(self, brojTacaka, maxY, maxX, maxZ):
        randomTacke = list()
        while len(randomTacke) < brojTacaka:
            randY = r.randrange(0, maxY)
            randX = r.randrange(0, maxX)
            randZ = r.randrange(0, maxZ)
            randomTacke.append(Tacka(randY, randX, randZ))
        return randomTacke

    def prikaziRasporedTacaka(self):
        plt.plot([t.y for t in self.tacke], [t.x for t in self.tacke], '.')
        plt.show()

    def srednjaVrednostPovrsi(self):
        suma = reduce(lambda a, b: a + b, [t.z for t in self.tacke])
        return suma / float(len(self.tacke))

    def minimalniObuhvatniPravougaonik(self):
        maxY = max([t.y for t in self.tacke])
        minY = min([t.y for t in self.tacke])
        maxX = max([t.x for t in self.tacke])
        minX = min([t.x for t in self.tacke])

        return [minY, minX, maxY, maxX]

    def __str__(self):
        mbr = self.minimalniObuhvatniPravougaonik()
        return 'Informacije o povrsi:' \
               '\n\tanaliticar: ' + self.analiticar +\
               '\n\tbroj tacaka povrsi: ' + str(self.brTacaka) + \
               '\n\tsrednja vrednost povrsi: {0:0.1f}'.format(self.srednjaVrednostPovrsi()) +\
               '\n\tMinimalni obuxvatni pravougaonik:' \
               '\n\t\tdonje levo teme: ({0:0.2f}, {1:0.2f})' \
               '\n\t\tgornje desno teme: ({2:0.2f}, {3:0.2f})'.format(mbr[0], mbr[1], mbr[2], mbr[3])
