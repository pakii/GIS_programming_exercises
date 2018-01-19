from datetime import datetime


class Osoba:
    def __init__(self):
        self.ime = ''
        self.prezime = ''
        self.datumRodjenja = None
        self.adresa = ''

    def unesiPodatke(self, ime, prezime, datumRodjenja, adresa):
        self.ime = ime
        self.prezime = prezime
        self.datumRodjenja = datetime.strptime(datumRodjenja, '%d.%m.%Y')
        self.adresa = adresa

    def __str__(self):
        return '\n\time: ' + self.ime + \
               '\n\tprezime: ' + self.prezime + \
               '\n\tdatum rodjenja: ' + str(self.datumRodjenja.day) + '.' + str(self.datumRodjenja.month) + '.' + \
               str(self.datumRodjenja.year) + '.' + \
               '\n\tadresa: ' + self.adresa


class Djak(Osoba):
    def __init__(self):
        Osoba.__init__(self)
        self.osnovnaSkola = ''
        self.odeljenje = ''
        self.godinaUpisa = None
        self.razred = 0

    def odrediRazred(self):
        for c in self.odeljenje:
            if c.isdigit():
                return c
            break

    def daLiJeObnovioGodinu(self):
        trenutnaGodina = datetime.now().year
        pretpostavljeniRazred = trenutnaGodina - self.godinaUpisa.year
        obnovljeneGodine = pretpostavljeniRazred - int(self.razred)
        if obnovljeneGodine > 0:
            return [True, obnovljeneGodine]
        else:
            return [False, obnovljeneGodine]

    def unesiPodatke(self, ime, prezime, datumRodjenja, adresa, osnovnaSkola, odeljenje, godinaUpisa):
        Osoba.unesiPodatke(self, ime, prezime, datumRodjenja, adresa)
        self.osnovnaSkola = osnovnaSkola
        self.odeljenje = odeljenje
        self.godinaUpisa = datetime.strptime(godinaUpisa, '%Y')
        self.razred = self.odrediRazred()

    def __str__(self):
        out = '\nPodaci o uceniku:' + Osoba.__str__(self) + \
              '\n\trazred: ' + str(self.razred) + '.' + \
              '\n\todeljenje: ' + str(self.odeljenje) + \
              '\n\tgodina upisa: ' + str(self.godinaUpisa.year) + '.'
        if self.daLiJeObnovioGodinu()[0]:
            out += '\n\tnapomena: Ucenik je obnovio ' + str(self.daLiJeObnovioGodinu()[1]) + ' godinu/e u toku ' \
                                                                                             'skolovanja.'
        return out


class Zaposleni(Osoba):
    def __init__(self):
        Osoba.__init__(self)
        self.kompanija = ''
        self.departman = ''
        self.datumZaposlenja = None
        self.prethodnaZaposlenja = []

    def unesiPodatke(self, ime, prezime, datumRodjenja, adresa, kompanija, departman, datumZaposlenja):
        Osoba.unesiPodatke(self, ime, prezime, datumRodjenja, adresa)
        self.kompanija = kompanija
        self.departman = departman
        self.datumZaposlenja = datetime.strptime(datumZaposlenja, '%d.%m.%Y')

    def unesiPodatkeOPrethodnimZaposlenjima(self, kompanija, pocetak, kraj):
        self.prethodnaZaposlenja.append(
            [kompanija, datetime.strptime(pocetak, '%d.%m.%Y'), datetime.strptime(kraj, '%d.%m.%Y')])

    def ukupniRadniStaz(self):
        prethodnoDani = 0
        for zapis in self.prethodnaZaposlenja:
            prethodnoDani += (zapis[2] - zapis[1]).days
        trenutnoVreme = datetime.now()
        stazUTrenutnojFirmi = (trenutnoVreme - self.datumZaposlenja).days

        return (prethodnoDani + stazUTrenutnojFirmi) / 30

    def __str__(self):
        out = '\nPodaci o zaposlenom:' + Osoba.__str__(self) + \
              '\n\tkompanija: ' + str(self.kompanija) + \
              '\n\tdepartman: ' + str(self.departman) + \
              '\n\tdatum zaposlenja: ' + str(self.datumZaposlenja.day) + '.' + str(self.datumZaposlenja.month) + '.' + \
              str(self.datumZaposlenja.year) + '.' + \
              '\n  Radno iskustvo:'
        if not self.prethodnaZaposlenja:
            out += '\n\tNema podataka o prethodnim zaposlenjima.'
        else:
            num = 0
            out += '\n\t komopanija:   od    -    do;'
            for a in self.prethodnaZaposlenja:
                num += 1
                out += '\n\t{0:d}. {1:s}: {2:d}.{3:d}.{4:d} - {5:d}.{6:d}.{7:d};'.format(num, a[0], a[1].day,
                                                                                         a[1].month,
                                                                                         a[1].year,
                                                                                         a[2].day, a[2].month,
                                                                                         a[2].year)
        return out
