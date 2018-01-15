# -*- coding: utf-8 -*-
import random as r

print '\t\tDZ2: Фундаменталне структуре података. Библиотека NumPy.\n'

# print '\n\t1. resenje:\n'
# #1. Написати програм која рачуна суму парних елемената низа. Тестирати га позивом из
# #главног програма.
#
# niz = [int(100*r.random()) for i in xrange(10)]#niz koji ce sluziti za testiranje
#
# sumEven = 0
# for x in niz:
# 	if x % 2 == 0:
# 		sumEven += x
# print 'Ulazni niz'
# print niz
# print "Suma elemenata koji su parni brojevi je "+str(sumEven)
#
# sumEvenPos = 0
# for i in range(0, len(niz), 2):
# 	sumEvenPos += niz[i]
#
# print "Suma elemenata parnim pozicijama "+str(sumEvenPos)
#
#
# print '\n\t2. resenje:\n'
# #2. Написати програм која рачуна суму елемената низа. Тестирати га позивом из главног
# #програма.
#
# print 'Ulazni niz'
# print niz
# sumNiz = reduce(lambda a, b: a+b, niz)
# print "Suma elemenata niza je "+str(sumNiz)
#
#
# print '\n\t3. resenje:\n'
# #3. Написати програм која рачуна производ елемената низа. Тестирати га позивом из
# #главног програма.
# print 'Ulazni niz'
# print niz
# proNiz = reduce(lambda a, b: a*b, niz)
# print "Proizvod elemenata niza je "+str(proNiz)
#
#
# print '\n\t4. resenje:\n'
# # 4. Написати програм која од два низа креира нови низ тако да елементи тог низа
# # представљају наизменична појављивања елемената првог и другог низа, односно
# # другог и првог низа у зависности од унете опције корисника (нпр. за унос опције -п
# # прво се ређају елементи првог па другог, а за унос опције -д прво се ређају елементи
# # другог па првог). Тестирати га позивом из главног програма.
#
# niz1 = ['*' for i in range(5)]
# niz2 = ['-' for i in range(5)]
# print 'Ovo su dva niza'
# print niz1, niz2
# print 'Sada se kreira novi niz od ova dva...'
#
# userInput = raw_input('Izaberite pocetni clan niza: p ili d')
# if userInput == 'п':
#     rez = niz1
#     for i in range(0, len(niz2), 2):
#         rez.insert(i + 1, niz2[i])
#     else:
#         rez.insert(len(rez) - 1, niz2[len(niz2) - 1])  # dodaj poslednji clan niza 'niz2' na pretposlednje mesto izlaznog niza
#     print rez
# elif userInput == 'д':
#     rez = niz2
#     for i in range(0, len(niz1), 2):
#         rez.insert(i + 1, niz1[i])
#     else:
#         rez.insert(len(rez) - 1, niz1[len(niz1) - 1])  # dodaj poslednji clan niza 'niz1' na pretposlednje mesto izlaznog niza
#     print rez
#
#
# print '\n\t5. resenje:\n'
# # 5. Написати програм који за унету реченицу приказује карактере који сe појављују у
# # њој.
#
# inputedSentence = raw_input('Unesite zadatu recenicu...').lower()
# slova = []
# cifre = []
# ostalo = []
# for c in inputedSentence:
#     if c.isalpha():
#         slova.append(c)
#     elif c.isdigit():
#         cifre.append(c)
#     else:
#         ostalo.append(c)
#
# slova = set(slova)
# slova = ','.join(slova)
# print('Slova koja se pojavljuju: '+slova)
# cifre = set(cifre)
# cifre = ','.join(cifre)
# print('Cifre koje se pojavljuju: '+cifre)
# ostalo = set(ostalo)
# ostalo = ''.join(ostalo)
# print('Ostali karakteri se pojavljuju: '+ostalo)
#
#
# print '\n\t6. resenje:\n'
# # 6. Написати програм који врши фитовање полинома произвољног степена кроз сет
# # унетих тачака (2Д простор). Корисник прво задаје број тачака кроз које провлачи
# # полином, затим уноси X, Y координате тачака. Након што су унете све тачке,
# # корисник дефинише степен полинома. Резултат у виду формуле полинома са
# # одређеним коефицијентима приказује се на стандардном излазу.
#
# import numpy as np
#
# brTac = input('Zadaj broj tacaka za fitovanje...')
# X = []
# Y = []
# for i in range(1, brTac + 1):
#     print 'Tacka %i:' % i
#     X.append(input('unesi X:'))
#     Y.append(input('unesi Y:'))
# stepen = input('Unesi stepen polinoma...')
# fitXY = np.polyfit(X, Y, stepen)
# formula = np.poly1d(fitXY)
# print 'Formula polinoma: %s' % str(formula)
#
#
print '\n\t7. resenje:\n'
# 7. Написати програм који имплементира игру Ајнц са једним играчем. Игра се са
# шпилом од 52 карте. На почетку играч уноси своје име након чега рачунар дели две
# карте играчу и две карте себи. У свакој следећој итерацији рачунар дели по једну
# карту играчу и себи. Циљ игре је сакупити карте које у збиру имају 21 поен. Карте са
# бројевима носе онолико бодова колики је број, док жандар, дама, краљ носе 10
# бодова. Карта Ас може да носи 1 или 10 бодова, у зависности од тога како играчу
# одговара. Играч који сакупи 21 је победио. Уколико играч премаши 21 бод, победник
# је његов противник. https://en.wikipedia.org/wiki/Blackjack

# pocetak igre
igracIme = raw_input('Unesite svoje ime...')
jednakZbir = False
nijeKrajIgranja = True
while nijeKrajIgranja:
    print('-----------------------------------------------------------------------------')
    igracKarte = []
    racunarKarte = []
    karte = ['as'] + [i for i in range(2, 11)] + [10, 10, 10]
    karte = karte * 4

    # deljenje karata
    igracPrvaKarta = r.choice(karte)
    karte.remove(igracPrvaKarta)
    igracDrugaKarta = r.choice(karte)
    karte.remove(igracDrugaKarta)

    if igracPrvaKarta == 'as' and igracDrugaKarta == 'as':
        igracKarte += [11, 1]
    elif igracPrvaKarta == 'as' and igracDrugaKarta != 'as':
        igracKarte += [11, igracDrugaKarta]
    elif igracPrvaKarta != 'as' and igracDrugaKarta == 'as':
        igracKarte += [igracPrvaKarta, 11]
    else:
        igracKarte += [igracPrvaKarta, igracDrugaKarta]

    print igracIme + ': ', igracKarte

    racunarPrvaKarta = r.choice(karte)
    karte.remove(racunarPrvaKarta)
    racunarDrugaKarta = r.choice(karte)
    karte.remove(racunarDrugaKarta)

    if racunarPrvaKarta == 'as' and racunarDrugaKarta == 'as':
        racunarKarte += [11, 1]
    elif racunarPrvaKarta == 'as' and racunarDrugaKarta != 'as':
        racunarKarte += [11, racunarDrugaKarta]
    elif racunarPrvaKarta != 'as' and racunarDrugaKarta == 'as':
        racunarKarte += [racunarPrvaKarta, 11]
    else:
        racunarKarte += [racunarPrvaKarta, racunarDrugaKarta]

    print 'racunar: ', [racunarPrvaKarta, '*']

    # ---logika jedne partije---

    # logika racunara
    zbirRacunara = reduce(lambda a, b: a + b, racunarKarte)
    # sve dok je zbir karata manji od 16 izvlaci jos jednu kartu
    while zbirRacunara <= 16:

        # --logika izvlacenja karata--
        izvucenaKarta = r.choice(karte)
        karte.remove(izvucenaKarta)

        # ako nije izvucen AS
        if izvucenaKarta != 'as':
            if zbirRacunara + izvucenaKarta > 21 and (11 in racunarKarte):
                racunarKarte.append(izvucenaKarta)
                racunarKarte.remove(11)
                racunarKarte.append(1)
            else:
                racunarKarte.append(izvucenaKarta)

            zbirRacunara = reduce(lambda a, b: a + b, racunarKarte)
        else:
            if (zbirRacunara + 11) > 21:
                racunarKarte.append(1)
            else:
                racunarKarte.append(11)

            zbirRacunara = reduce(lambda a, b: a + b, racunarKarte)

    # logika igraca
    zbirIgraca = reduce(lambda a, b: a + b, igracKarte)
    nijeKrajPartije = True
    while nijeKrajPartije:
        # ako igrac na pocetku ima 21, momentalno pobedjuje
        if (igracKarte[0] + igracKarte[1]) == 21:
            nijeKrajPartije = False
        else:
            hitOrStay = raw_input('Za "hit" unesite h; za "stay" unesite s...').lower()
            if hitOrStay == 'h':
                # --logika izvlacenja karata--
                izvucenaKarta = r.choice(karte)
                karte.remove(izvucenaKarta)

                # ako nije izvucen AS
                if izvucenaKarta != 'as':
                    if zbirIgraca + izvucenaKarta > 21 and (11 in igracKarte):
                        igracKarte.append(izvucenaKarta)
                        igracKarte.remove(11)
                        igracKarte.append(1)
                    else:
                        igracKarte.append(izvucenaKarta)

                    zbirIgraca = reduce(lambda a, b: a + b, igracKarte)
                else:
                    if (zbirIgraca + 11) > 21:
                        igracKarte.append(1)
                    else:
                        igracKarte.append(11)

                    zbirIgraca = reduce(lambda a, b: a + b, igracKarte)

                print igracIme + ': ', igracKarte, zbirIgraca

                # slucaj kada igrac ima jednako ili preko 21
                if zbirIgraca > 21:
                    nijeKrajPartije = False
                    print('IZGUBILI STE...')
                    print('-----------------------------------------------------------------------------')

                elif zbirIgraca == 21 and zbirRacunara != 21:
                    nijeKrajPartije = False
                    print 'racunar: ', racunarKarte, zbirRacunara
                    print('POBEDILI STE...')
                    print('-----------------------------------------------------------------------------')
            # igrac bira stay sto znaci da ima ili tacno ili manje 21
            elif hitOrStay == 's':
                nijeKrajPartije = False
                zbirIgraca = reduce(lambda a, b: a + b, igracKarte)
                print igracIme + ': ', igracKarte, zbirIgraca
                print 'racunar: ', racunarKarte, zbirRacunara

                if zbirIgraca == 21 and zbirRacunara != 21:
                    print('POBEDILI STE...')
                    print('-----------------------------------------------------------------------------')

                elif zbirIgraca == zbirRacunara and zbirRacunara <= 21:  # igrac i rac su jednaki
                    jednakZbir = True

                elif zbirIgraca > zbirRacunara and zbirRacunara < 21:  # igrac vise od rac i rac nije presao 21
                    print('POBEDILI STE...')
                    print('-----------------------------------------------------------------------------')

                elif zbirIgraca < zbirRacunara <= 21:  # igrac manje i racunar nije presao 21
                    print('IZGUBILI STE...')
                    print('-----------------------------------------------------------------------------')
            # resavanje slucaja kada su zbirovi karata jednaki
            if jednakZbir:
                if max(igracKarte) == max(racunarKarte):
                    print('NERESENO')
                if max(igracKarte) < max(racunarKarte):
                    print('IZGUBILI STE...')

    josJednaPartija = raw_input('Za jos jednu partiju unesite "da" ili bilo sta drugo da zavrsite igru...').lower()
    if josJednaPartija == 'da':
        nijeKrajIgranja = True
        nijeKrajPartije = True
    else:
        nijeKrajIgranja = False
