from Sfera import Sfera

Sfera.ukupanBrojKreiranihObjekata()

sfera = Sfera(4.0)
globus = Sfera(12, 1.0, 1.0, 1.0)
bilijarska_lopta = Sfera(10.0, 10.0, 0.0)
jedinicna_sfera = Sfera()

Sfera.ukupanBrojKreiranihObjekata()

print('Zapremine kreiranih objekata')
print '\tsfera: ' + str(sfera.izracunajZapreminu)
print '\tglobus: ' + str(globus.izracunajZapreminu)
print '\tbilijarska_lopta: ' + str(bilijarska_lopta.izracunajZapreminu)
print '\tjedinicna_sfera: ' + str(jedinicna_sfera.izracunajZapreminu)
