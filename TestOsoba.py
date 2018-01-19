from Osoba import Djak
from Osoba import Zaposleni

# kreiranje objekata
djak1 = Djak()
djak2 = Djak()
zaposleni1 = Zaposleni()
zaposleni2 = Zaposleni()

djak1.unesiPodatke('Dusan',
                   'Petkovic',
                   '17.7.1994',
                   'Mije Kovacevica 7b',
                   'O.S. J.J.Zmaj',
                   '5-4',
                   '2012')
print(djak1)
print djak1.odrediRazred()
print djak1.daLiJeObnovioGodinu()[0]  # ova metoda vraca niz ciji je prvi clan bool a drugi iznos obnovljenih godina

# djak2.unesiPodatke(raw_input('ime:'),
#                    raw_input('prezime:'),
#                    raw_input('unesite datum rodjenja ucenika u formatu dan.mesec.godina (pr: 17.7.1994)'),
#                    raw_input('adresa:'),
#                    raw_input('naziv skole:'),
#                    raw_input('unesite odeljenje u formatu razred / broj odeljenja (pr: 4 / 2)'),
#                    raw_input('godina upisa:'))
#
# print(djak2)

zaposleni1.unesiPodatke('Aleksandar',
                        'Pavlovic',
                        '29.8.1994',
                        'Mije Kovacevica 7b',
                        'Levi9',
                        'JavaScript department',
                        '1.12.2017')

zaposleni1.unesiPodatkeOPrethodnimZaposlenjima('Google', '1.12.2013', '1.11.2017')
print(zaposleni1)
print('Ukupan radni staz zaposlenog iznosi ' + str(zaposleni1.ukupniRadniStaz())) + ' meseci.'

# zaposleni2.unesiPodatke(raw_input('ime:'),
#                         raw_input('prezime:'),
#                         raw_input('unesite datum rodjenja ucenika u formatu dan.mesec.godina (pr: 17.7.1994)'),
#                         raw_input('adresa:'),
#                         raw_input('kompanija:'),
#                         raw_input('department: '),
#                         raw_input('unesite datum zaposljavanja u formatu dan.mesec.godina (pr: 17.7.1994)')
#                         )
# print zaposleni2
