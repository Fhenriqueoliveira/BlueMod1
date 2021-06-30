#2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) 
#e seus valores correspondentes aos quadrados desses números.

vl_num = [1,4,5,6,7,9]
dicionario ={}

for i in vl_num:
    dicionario [i] = i*i
print (dicionario)    

print('Exercicio 2 --------------------------------------------------------------------------------------------')
print('****' * 50)
print('****' * 50)
#b – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.​

numeros ={}
for i in range(1,11):
    numeros[i]= i*i
print(numeros)    

print('Exercicio 3 --------------------------------------------------------------------------------------------')
print('****' * 50)
print('****' * 50)

### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.
produto = {'refrigerante': 'coca','carne': ' alcatra', 'calada': 'cebola'}
quantidade = {'refrigerante': 3, 'Carne': 2, 'Salada':5}
print(f'Nossos produtos:\n {produto.keys()}')
prod= input('Qual produto vc deseja?').lower()
if produto.keys == prod:
    produto.get(prod,'Desculpa, não temos esse produto em nosso estoque')
    
#print(f'Hoje no mercado temos:\n {estoque.keys()}')
#compra = input('Qual produto você vair querer comprar?')