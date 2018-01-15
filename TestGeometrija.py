# coding=utf-8
from Geometrija import Tacka
from Geometrija import Duz

# Креирање две тачке (почетак (x_poc, y_poc) и крај (x_zav, y_zav)) на основу уноса корисника са стандардног улаза;
# Креирање дуж чија су почетна и крајња тачка баш ове задате тачке;
# Креирање друге дуж са задатим координатама почетне и крајње тачке;
# Испис које дужи су формиране;
# Померање тачке крај за (dx, dy) на основу уноса корисника са стандардног улаза;
# Испис нове дуж.
print('Kreiranje duzi:')
xp = input('Unesite x-koordinatu pocetne tacke...')
yp = input('Unesite y-koordinatu pocetne tacke...')
xk = input('Unesite x-koordinatu krajnje tacke...')
yk = input('Unesite x-koordinatu krajnje tacke...')

pocetak = Tacka(xp, yp)
kraj = Tacka(xk, yk)

duz1 = Duz(pocetak, kraj)
duz2 = Duz.duzKoor(1, 1, 4, 5)

print('Formirane su sledece duzi: ')
print ' \nduz 1:' + str(duz1)
print ' \nduz 2:' + str(duz2)

dx = input('Unesite pomeraj po x-osi...')
dy = input('Unesite pomeraj po y-osi...')

kraj.pomeriZa(dx, dy)

print '\nKrajnja tacka prve duzi je pomerena za {0:d} po x - osi i za {1:d} po y - osi'.format(dx, dy)
print ' duz 1:' + str(duz1)


