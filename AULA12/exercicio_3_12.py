#3. Faça um programa que leia nome e média de um aluno, guardando também a situação
#em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
#aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
#reprovado

new=1
aluno= dict()
aluno['nome'] = input('Nome do Aluno: ')
aluno['media']= float(input('Média do aluno: ').replace(',','.'))
if aluno['media'] >= 7.0:
    aluno['situacao']= 'Aprovado'
elif aluno['media'] <=6.9 or aluno['media']>= 5.0:
        aluno['situacao']= 'Recuperação'
else:
     aluno['situacao']= 'Reprovado'
print('==='*30)     
for chave, valor in aluno.items():
        print(f'{chave} - {valor} ')
