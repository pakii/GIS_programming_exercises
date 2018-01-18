class Inzenjer:
    def __init__(self, ime, prezime, JMBG, licenca=''):
        self.ime = ime
        self.prezime = prezime
        self.JMBG = JMBG
        self.licenca = licenca

    # getteri
    def __dajIme__(self):
        return self.ime

    def __dajPrezime__(self):
        return self.prezime

    def __dajJMBG__(self):
        return self.JMBG

    def __dajLicencu__(self):
        return self.licenca

    # setteri
    def __setIme__(self, vrednost):
        self.ime = vrednost

    def __setPrezime__(self, vrednost):
        self.prezime = vrednost

    def __setJMBG__(self, vrednost):
        self.JMBG = vrednost

    def __setLicenca__(self, vrednost):
        self.licenca = vrednost

    def __str__(self):
        return 'ime: ' + self.ime + \
               '\nprezime: ' + self.prezime + \
               '\nJMBG: ' + str(self.JMBG)


class GeodetskiInzenjer(Inzenjer):
    def __init__(self, ime, prezime, JMBG, godineRadnogStaza, licenca=''):
        Inzenjer.__init__(self, ime, prezime, JMBG, licenca)
        self.godineRadnogStaza = godineRadnogStaza

    # getter
    def __dajGodineRadnogStaza__(self):
        return self.godineRadnogStaza

    # setter
    def __setIme__(self, vrednost):
        self.godineRadnogStaza = vrednost

    def __str__(self):
        izl = Inzenjer.__str__(self) + '\nbroj godina radnog staza: ' + str(self.__dajGodineRadnogStaza__())
        if self.licenca == '':
            return izl + \
                   '\nlicenca: nema licencu.'
        else:
            return izl + \
                   '\nlicenca: ' + self.licenca


class ElektrotehnickiInzenjer(Inzenjer):
    def __init__(self, ime, prezime, JMBG, brojOdradjenihProjekata, licenca=''):
        Inzenjer.__init__(self, ime, prezime, JMBG, licenca)
        self.godineRadnogStaza = brojOdradjenihProjekata

    # getter
    def __dajBrojOdradjenihProjekata__(self):
        return self.brojOdradjenihProjekata

    # setter
    def __setIme__(self, vrednost):
        self.brojOdradjenihProjekata = vrednost

    def __str__(self):
        izl = Inzenjer.__str__(self) + '\nbroj projekata na kojima je radio: ' + str(
            self.__dajBrojOdradjenihProjekata__())
        if self.licenca == '':
            return izl + \
                   '\nlicenca: nema licencu.'
        else:
            return izl + \
                   '\nlicenca: ' + self.licenca

    # Ovo za licencu je moglo da se napise u nadklasi, ali u zadatku je sprecificirano da treba ovako


# testiranje
instanca = GeodetskiInzenjer('Aleksandar', 'Pavlovic', 47328293, 0.1)
print str(instanca)
