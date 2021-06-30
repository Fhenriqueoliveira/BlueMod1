#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
#o maior e o menor peso lidos.
'''
maior_peso = 0 #declarando variaveis
menor_peso = 0 #declarando variaveis
for pessoa in range(1,6): # a cada pessoa atribuindo um range até a 5 pessoa.
    peso = float(input('Peso da {}º pessoa: '.format(pessoa))) #input para receber 5x o peso das pessoas
    if pessoa == 1:
       maior_peso = peso
       menor_peso = peso     
    else:    
       if peso > maior_peso:
          maior_peso = peso
       if peso < menor_peso:
          menor_peso = peso
print('O maior peso foi {}Kg'.format(maior_peso))
print(maior_peso)
print('O menor peso foi {}Kg'.format(menor_peso))
print(menor_peso)    






#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
#tabuada desse número.


resp= int(input('Escolha um numero para gerar a tabuada! :'))
while resp < 1:
    resp = int(input('Zero nao pode né amigão, escolhe outro numero ai!!'))
for num in range(1,11):
    print(f'{resp} X {num} = {num*resp}')


    #03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
     #mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maior_idade = 0 #declarando variaveis
menor_idade = 0 #declarando variaveis
for pessoa in range(1,8): # a cada pessoa atribuindo um range até a 7 pessoa.
    idade = int(input('Digite a idade da {}º pessoa: '.format(pessoa))) #input para receber 7x a idade das pessoas
    if idade >= 18: #Se a idade digitada for maior ou igual a 18, então variavel maior_idade recebe +1
       maior_idade += 1
    else:
       menor_idade +=1 #Senão a variavel menor_idade recebe +1


print(f'{maior_idade} pessoas são maiores de idade')
print(f'{menor_idade} pessoas são maiores de idade')
       
       '''
#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
#apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
#Mostre também quantos valores pares foram digitados.

soma = 0
qt_num=0
for num in range(1,7):
    entrada = int(input('Digite o {}º numero par: '.format(num)))
    if entrada % 2 ==0:
        soma += entrada
        qt_num += 1
print(f'Foram digitados {qt_num} numeros pares e a soma deles é {soma}')



