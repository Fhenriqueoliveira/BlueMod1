#listas
#1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
#a) tamanho da lista.
#b) maior valor da lista.
#c) menor valor da lista.
#d) soma de todos os elementos da lista.
#e) lista em ordem crescente.
#f) lista em ordem decrescente.


L = [5, 7, 2, 9, 4, 1, 3]
print (f'A lista tem {len(L)} elementos') # a) tamanho da lista.
print (f'O {max(L)} é o maior elemento da lista') # b) maior valor da lista.
print (f'O {min(L)} é o menor elemento da lista') # c) menor valor da lista.
print (f'A soma dos elementos da lista é igual a  {sum(L)} ') # d) soma de todos os elementos da lista.
L.sort()
print (f'Essa é a ordem crescente da lista  {[L]} ') # e) lista em ordem crescente
L.reverse()
print (f'Essa é a ordem decrescente da lista  {[L]} ') # f) lista em ordem decrescente


#2- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
#perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a
#pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
#como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".
#3- Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
#escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.



