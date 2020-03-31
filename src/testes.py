# este eh o programa de testes dos numeros primos

import primo

cont = 1
num = 2
while cont < 101:
    if primo.ehprimo(num) == True:
        print(num)
        cont += 1
    num = num + 1

