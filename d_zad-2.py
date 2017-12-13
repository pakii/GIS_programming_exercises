# -*- coding: utf-8 -*-
print '\t\tDZ2: Фундаменталне структуре података. Библиотека NumPy.\n'
print '\t1. resenje:\n'
#1. Написати програм која рачуна суму парних елемената низа. Тестирати га позивом из
#главног програма.
import random as r
niz = [int(100*r.random()) for i in xrange(10)]
sumEven = 0
for x in niz:
	if x % 2 == 0:
		sumEven += x
print 'Ulazni niz'
print niz
print "Suma elemenata koji su parni brojevi je "+str(sumEven)

sumEvenPos = 0
for i in range(0, len(niz), 2):
	sumEvenPos += niz[i]

print "Suma elemenata parnim pozicijama "+str(sumEvenPos)

print '\n\t2. resenje:\n'
#2. Написати програм која рачуна суму елемената низа. Тестирати га позивом из главног
#програма.

print 'Ulazni niz'
print niz
sumNiz = reduce(lambda a, b: a+b, niz)
print "Suma elemenata niza je "+str(sumNiz)


print '\n\t3. resenje:\n'
#3. Написати програм која рачуна производ елемената низа. Тестирати га позивом из
#главног програма.
print 'Ulazni niz'
print niz
proNiz = reduce(lambda a, b: a*b, niz)
print "Proizvod elemenata niza je "+str(proNiz)


print '\n\t4. resenje:\n'
#4. Написати програм која од два низа креира нови низ тако да елементи тог низа
#представљају наизменична појављивања елемената првог и другог низа, односно
#другог и првог низа у зависности од унете опције корисника (нпр. за унос опције -п
#прво се ређају елементи првог па другог, а за унос опције -д прво се ређају елементи
#другог па првог). Тестирати га позивом из главног програма.
niz1 = ['*' for i in range(5)]
niz2 = ['-' for i in range(5)]
print 'Ovo su dva niza'
print niz1, niz2
print 'Sada se kreira novi niz od ova dva...'

userInput = raw_input('Izaberite pocetni clan niza: p ili d')
if userInput == 'p':
	rez = niz1
	for i in range(0, len(niz2), 2):
		rez.insert(i+1, niz2[i])
	else:
		rez.insert(len(rez)-1, niz2[len(niz2)-1])
	print rez
else:
	rez = niz2
	for i in range(0, len(niz1), 2):
		rez.insert(i+1, niz1[i])
	else:
		rez.insert(len(rez)-1, niz1[len(niz1)-1])
	print rez

print '\n\t5. resenje:\n'
#5. Написати програм који за унету реченицу приказује карактере који сe појављују у
#њој.


print '\n\t6. resenje:\n'
#6. Написати програм који врши фитовање полинома произвољног степена кроз сет
#унетих тачака (2Д простор). Корисник прво задаје број тачака кроз које провлачи
#полином, затим уноси X, Y координате тачака. Након што су унете све тачке,
#корисник дефинише степен полинома. Резултат у виду формуле полинома са
#одређеним коефицијентима приказује се на стандардном излазу.

import numpy as np
brTac = input('Zadaj broj tacaka za fitovanje...')
X = []
Y = []
for i in range(1, brTac+1):
	print 'Tacka %i:' % i
	X.append(input('unesi X:'))
	Y.append(input('unesi Y:'))
stepen = input('Unesi stepen polinoma...')
fitXY = np.polyfit(X, Y, stepen)
formula = np.poly1d(fitXY)
print 'Formula polinoma: %s' % str(formula)
print '\n\t7. resenje:\n'
#7. Написати програм који имплементира игру Ајнц са једним играчем. Игра се са
#шпилом од 52 карте. На почетку играч уноси своје име након чега рачунар дели две
#карте играчу и две карте себи. У свакој следећој итерацији рачунар дели по једну
#карту играчу и себи. Циљ игре је сакупити карте које у збиру имају 21 поен. Карте са
#бројевима носе онолико бодова колики је број, док жандар, дама, краљ носе 10
#бодова. Карта Ас може да носи 1 или 10 бодова, у зависности од тога како играчу
#одговара. Играч који сакупи 21 је победио. Уколико играч премаши 21 бод, победник
#је његов противник. https://en.wikipedia.org/wiki/Blackjack
