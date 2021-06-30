#Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, crie um lançador de dados e moedas em que o usuário deve escolher 
#o objeto a ser lançado. Não esqueça que os lançamentos são feitos de forma randômica.

from random import randint
class lancador:
    def __init__(self):
        self.lado = ''
    
    def jogar_moeda(self):
        if randint(0,1)==0:
            self.lado='Cara'
        else:
            self.lado='Coroa'
        return self.lado
  
    def jogar_dados(self):
        jogada = randint(1,6)
        self.lado = jogada
        return self.lado

while True:
    jogo= int(input('Qual jogo vc gostaria de jogar?\n [1- Cara ou cora] [2-Dados] [0-Sair]'))
    if jogo == 0:
        break
    while jogo ==1:
       if jogo ==1:    
          moeda = lancador()
          print(moeda.jogar_moeda())
          jogo=int(input('Deseja jogar novamente?\n [1/sim] [0/Não]: '))
          
         
    while jogo == 2:                    
        if jogo ==2:
           dado= lancador()
           print(dado.jogar_dados())        
           jogo=int(input('Deseja jogar novamente?\n [2/sim] [0/Não]: '))                    
    else:
        print('Obrigado pela partida')
        
        