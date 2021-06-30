from random import randint
numeros =list()
listanova =list()
jogos = 1
p=int(input('Quantos jogos? '))
while jogos <= p:
    count = 0
    while True:
        num = randint(1,60)
        if num not in numeros: 
            numeros.append(num)
            count +=1
        if count >= 6:
            jogos +=1
            break
        
    numeros.sort()
    listanova.append(numeros)
    numeros=[]
print(listanova)    
    
    