#DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
#lista. No final, mostre:
#A) Quantas pessoas estão cadastradas.
#B) A média da idade.
#C) Uma lista com as mulheres.
#D) Uma lista com as idades que estão acima da média.
#OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
#perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

dados_geral = {}
lista_geral=[]
while True:
    dados_geral['nome']=input('Digite seu nome: ')
    while True:
        dados_geral['sexo']=input('Digite seu sexo: [F\M] ').upper()
        if dados_geral['sexo'] in 'MF':
             break
        print('opção invalida! digite apenas M ou F')
    dados_geral['idade']=int(input('Digite sua idade: '))
    while i !='N':
        i = input('Quer continuar? [S\N]')
print(dados_geral)    