import matplotlib.pyplot as plt
from StatistickeAnalizePovrsiTerena import Tacka
from StatistickeAnalizePovrsiTerena import Povrs

povrs = Povrs(raw_input('Unesite vase ime...'), input('Unesite broj tacaka povrsi'), 1000, 1000, 100)

print(povrs)  # stampanje podataka o kreiranoj povrsi

print povrs.tacke[input('Provera da li se oznake tacaka korektno dodeljuju:\nuunesite redni broj tacke...')].oznaka

# ****testiranje proracuna najblize tacke****
# kreiranje nove tacke
tacka = Tacka(554.23, 233.53)

# proracun najblize tacke na povrsi
najbliza = tacka.najblizaTacka(povrs.tacke)
print 'Poziciji (' + str(tacka.y) + ', ' + str(tacka.x) + ') najbliza je tacka na povrsi je ' + str(najbliza) + '.'
# dodaj novokreiranu tacku u plot-u
plt.plot(tacka.y, tacka.x, '.')
plt.plot()

# ****testiranje interpolacije****
t1 = Tacka(10, 10, 20)
t2 = Tacka(20, 20, 40)

plt.plot([t1.y, t2.y], [t1.x, t2.x], '.')

interpolovana = Tacka(15, 15)
interpolovana.interpolacijaNaPravcuIzmedju(t1, t2)

plt.plot(interpolovana.y, interpolovana.x, '.')
povrs.prikaziRasporedTacaka()  # prikaz plota tacaka povrsi
