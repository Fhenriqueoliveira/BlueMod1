quantidade_sacar = int(input('Qual a quantidade que gostaria de sacar?'))
n100 = 0
n50 = 0
n10 = 0
n5 = 0
n1=0
while quantidade_sacar < 10 or quantidade_sacar >600:
      quantidade_sacar = int(input('O valor não é permitido, digite apenas entre R$10 e R$600: '))

quantidade_auxiliar = quantidade_sacar
n100 = quantidade_auxiliar // 100
quantidade_auxiliar = quantidade_auxiliar - (n100*100)
print (quantidade_auxiliar)
n50 = quantidade_auxiliar // 50
quantidade_auxiliar = quantidade_auxiliar - (n50*50)
print (quantidade_auxiliar)
n10 = quantidade_auxiliar // 10
quantidade_auxiliar = quantidade_auxiliar - (n10*10)
print (quantidade_auxiliar)
n5 = quantidade_auxiliar // 5
quantidade_auxiliar = quantidade_auxiliar - (n5*5)
print (quantidade_auxiliar)
n1 = quantidade_auxiliar // 1

print (quantidade_sacar)
if n100 > 0:
    print(f'quantidade de nota de R$100 é {n100}')
if n50 > 0:
    print(f'quantidade de nota de R$50 é {n50}')
if n10 > 0:
    print(f'quantidade de nota de R$10 é {n10}')
if n5 > 0:
    print(f'quantidade de nota de R$5 é {n5}')
if n1 > 0:
    print(f'quantidade de nota de R$1 é {n1}')