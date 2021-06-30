#Vamos aprimorar o código:  cadastro de jogador de futebol.py que foi desenvolvido no Code Lab da aula 14. 
#Faça com que o seu código funcione para vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador. 
from random import randint
class lancador:
    def __init__(self,item):
        self.item = item
        

    def jogar(self):
         #self.lado = jogo  
         if self.item == 1:
             return self.jogar_moeda()
              
         else: 
             return self.jogar_dados()      
    
    def jogar_moeda(self):
    
        if randint(0,1)==0:
            return 'Cara'
        else:
            return 'Coroa'
        
  
    def jogar_dados(self):
        
        return randint(1,6)
        
        

play = int(input('qual jogo quer jogar?'))
jogo =lancador(play)
print(jogo.jogar()) 
