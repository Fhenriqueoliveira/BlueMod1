#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário
#receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade
#, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve
#contribuir por 35 anos para se aposentar.

from datetime import datetime
cadastro=dict()
cadastro['nome'] = input('Digite o nome: ')
dt_nasc=int(input('Digite o ano de nascimento: '))
cadastro['idade'] = (datetime.now().year - dt_nasc)  
cadastro['carteira'] = int(input('Digite o numero da sua carteira de trabalho:'))
if cadastro['carteira'] != 0:
    cadastro['ano_contratacao']= int(input('Em que ano foi contratado: '))
    cadastro['salario']= float(input('Digite o salário: R$'))
    cadastro['idade_aposentadoria']= (((cadastro['ano_contratacao']+35)-datetime.now().year) + cadastro['idade'])
print('==='*30)    
print(f"-- Hoje o {cadastro['nome']} tem {cadastro['idade']} anos de idade e irá se aposentar com {cadastro['idade_aposentadoria']} anos.")     