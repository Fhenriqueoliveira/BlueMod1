#lista = [('Fabio', '4411-5247'), ('Bethania','114412-4515'),('juliana','4412-7859'),('Fabricio', '4411-0001'), ('felipi','9974-8547'),('joao','4411-9874')]
#contatos = dict(lista)
#nome = input('Digite o nome do contato:')
#print(contatos.get(nome,'Desculpa, não encontramos seu contato.'))



avengers = {'Chris Evans': 'Capitão América', 'Mark Ruffalo' : 'Hulk',
'Tom Hiddleston' : 'Loki', 'Chris Hemworth' : 'Thor', 'Robert Downey Jr' :'Homem de Ferro', 'Scarlett Johansson ': 'Viúva Negra' }
#ator= input('Qual o nome do ator?')
print('Chris Hemworth' in avengers.keys())#Verifica se a chave esta no dicionario
print('-------' *50)
print('Hulk' in avengers.values())#Verifica se o valor esta no dicionario
#print(avengers.get(ator),'Não localizamos o ator')
print('-------' *50)
print(avengers)
print('-------' *50)
print(type(avengers))
avengers ['Tom Holland'] = 'Homem Aranha'
print('-------' *50)
print(avengers)
print('-------' *50)
print(avengers.items())
del avengers['Tom Hiddleston']
print('-------' *50)
print(avengers)

print('****' * 50)
print('****' * 50)
print('****' * 50)
print('****' * 50)
print('****' * 50)
print('****' * 50)

