from random import randint
numeros =list()
lista =list()
count = 0
jogos = 0
p=int(input('Quantos jogos? '))
while jogos <= p:
    while True:
        num = randint(1,60)
        if num not in numeros: 
            numeros.append(num)
        if count >= 6:
            break
    numeros.sort()
    lista.append(numeros[:])
    numeros.clear()
    print(numeros)           