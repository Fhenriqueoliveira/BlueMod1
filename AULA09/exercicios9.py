
numeros = list()
while True:
    pergunta=int(input('Digite um Valor: '))
    if pergunta not in numeros:
        numeros.append(pergunta)
        print('Numero Adcionado!')    
    
    else:
        print('Valor Duplicado, Digite outro')


    resposta= input('Deseja imprimir os numeros ou quer continuar? [I/C]: ')
    for i in resposta:
        if i not in 'IiCc':
            resposta= input('Deseja imprimir os numeros ou quer continuar? [I/C]: ')
    if resposta in 'Ii':
         break
print(numeros)
#-----------------------------------------------------
lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número maior que ZERO: (0 para sair) ')))
    if lista[-1] == 0:
        lista.pop()
        break

    if lista[-1] % 2 == 0:
        par.append(lista[-1])
    else:
        impar.append(lista[-1])

print(f'''Lista: {lista}
Par: {par}
Impar: {impar}''')
#-----------------------------------------------------
num=list()
par=list()
impar=list()
while True:
    n=int(input('Digite um número: (digite "sair" para sair): ').lower().replace("sair","0"))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if n == 0:
        break
print (num)
print (par)
print (impar)
