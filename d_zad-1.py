# -*- coding: utf-8 -*-
print '\t\tDZ1: Синтакса језика. Типови података. Основне алгоритамске структуре.\n'
print '\t1. resenje:\n'
# 1. Написати програм који на стандардни излаз исписује текст “Здраво, геоинформатичари!” (ћириличним писмом)
print 'Здраво, геоинформатичари!\n'
print '\t2. resenje:\n'
# 2. Написати програм који за унета два цела броја на стандардни излаз исписује
    #најпре унете вредности, а затим и њихов збир, разлику, производ, цео део при
    #дељењу првог броја другим бројем и остатак при дељењу првог броја другим
    #бројем. Претпоставити да је унос коректан, тј. да друга унета вредност није 0, као
    #и да се уносе целобројне вредности са стандардног улаза.

num1 = int(raw_input('Unesite ceo broj: '))
num2 = int(raw_input('Unesite drugi ceo broj: '))
print 'Prvi uneti broj je {0:d}, a drugi {1:d}.\nNjihov zbir iznosi: {2:d}'.format(num1, num2, num1+num2)
print 'Razlika: '+str(num1 - num2)
print 'Proizvod: '+str(num1 * num2)
print 'Ceo deo pri deljenju prvog sa drugim: '+str(num1 / num2)
print 'Ostatak pri deljenju prvog sa drugim: '+str(num1 % num2)

print '\t3. resenje:\n'
#3. Написати програм који за унете вредности два правца у облику
    #степени : минути : секунде, исписује угао који та два правца граде. Угао треба да
    #буде у децималном запису, заокружен на 4 децимале.
print 'Unesi stepene minute i sekunde desnog pravca: '
RDir = [input('Unesi stepene: '), input('Unesi minute: '), input('Unesi sekunde: ')]
print 'Unesi stepene minute i sekunde levog pravca: '
LDir = [input('Unesi stepene: '), input('Unesi minute: '), input('Unesi sekunde: ')]

decRD = RDir[0] + RDir[1]/60.0 + RDir[2]/3600.0
decLD = LDir[0] + LDir[1]/60.0 + LDir[2]/3600.0

print 'Ugao izmedju unetih pravaca iznosi {0:0.4f} stepeni.'.format(decRD-decLD)

print '\t4. resenje:\n'
#4. Са стандардног улаза се уносе два четвороцифрена броја. Написати програм који
    #на стандардни излаз исписује суму цифара другог броја, а потом и разлику збира
    #цифара првог броја на парним и непарним позицијама.

print 'Unesite dva cetvorocifrena broja: '
num11 = raw_input('Unesite prvi broj: ')
num22 = raw_input('Unesite drugi ceo broj: ')
sumDigitsSecond = 0
for x in num22:
    sumDigitsSecond += int(x)
print 'Suma cifara drugog unetog broja je %d' % sumDigitsSecond
sumOdd = 0
sumEven = 0
for x in range(0, len(num11)):
    if int(x) % 2 == 0:
        sumOdd += int(num11[x]) #posto iteracija krece od nulte a ne prve pozicije
    else:
        sumEven += int(num11[x])
print 'Razlika zbira parnih i neparnix cifara prvog unetog broja iznosi %d' % (sumEven-sumOdd)

print '\t5. resenje:\n'
#5. Написати програм који за унети петоцирени број исписује његову највећу цифру.

fDigits = raw_input('Unesite petocifreni broj: ')
bigestDigit = -1
for x in fDigits:
    if int(x) > bigestDigit:
        bigestDigit = int(x)

print 'Najveca cifra unetog broja je %d.'% bigestDigit

print '\t6. resenje:\n'
#6. Програм учитава пет карактера. Исписати колико пута су се појавиле цифре.
fChars = raw_input('Unesite pet karaktera: ')
count = 0
for x in fChars:
    if x.isdigit():
        count += 1
print 'Cifra se pojavila %d puta.' %count


print '\t7. resenje:\n'
#7. Написати програм који испитује да ли се дата тачка М(Xm, Ym) налази унутар
    #троугла чија су темена тачке А(x1, y1), B(x2, y2) и C(x3, y3) и исписује одговор
    #ДА или НЕ.


print '\t8. resenje:\n'
#8. Написати програм који имплементира игру ”Погоди број”. На почетку игре
    #рачунар замишља један случајан број у интервалу [0,100]. Након тога играч уноси
    #своје име и започиње игру. Играч уноси један по један број све док не погоди који
    #број је рачунар замислио. Сваки пут када играч унесе број, у зависности од тога
    #да ли је број који је унет већи или мањи од замишљеног броја исписује се
    #одговарајућа порука. Игра се завршава у тренутку када играч погодио замишљен
    #број, када се на стандардном излазу приказује број покушаја из којег је број
    #погођен

import random as r
rand = r.randint(0, 100)
name = raw_input('Unesite svoje ime: ')
print 'Zamislio sam broj u intervalu od 0 do 100.\nPogodi koji je to broj...'
tryCount = 0
notCorrect = True
while notCorrect:
    guess = raw_input('Unesite broj u intervalu od 0 do 100: ')
    tryCount += 1
    print 'pokusaj %d' % tryCount
    if int(guess) == rand:
        print ':D\nBRAVO! Pogodili ste iz %d. pokusaja' % tryCount
        notCorrect = False
    elif int(guess) < rand:
        print ':/\n Promasili ste, pokusajte sa nekim vecim brojem.'
    elif int(guess) > rand:
        print ':/\n Promasili ste, pokusajte sa nekim manjim brojem.'

