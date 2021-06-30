from random import randint
jogos = 0
empates =0
cpu=0
usuario=0
new_game = 1
acoes =('PEDRA', 'PAPEL','TESOURA')
qt_jogos=  int(input('Quantos jogos vamos jogar?? '))
print('***'*20)
print('Suas opçoes:')
print(' [0] PEDRA \n [1] PAPEL \n [2] TESOURA')
print('***'*20)

while new_game == 1:
       while jogos < qt_jogos:
        
             for i in range(qt_jogos):     
                 jogador = int(input('Qual a sua jogada?'))
                 jogadaComputador = randint(0,2)  
                 jogos +=1    
            
                 if jogadaComputador == 0:
                     if jogador == 0:
                         print('EMPATAMOS!!')
                         empates +=1
                     elif jogador == 1:
                         print('Tá bom, vc ganhou ')
                         usuario +=1
                     elif jogador == 2:
                         print ('HÁÁÁÁ... GANHEIIIII')
                         cpu +=1    
                     
                              
                 elif jogadaComputador == 1:    
                         if jogador == 1:
                             print('EMPATAMOS!!')
                             empates +=1
                         elif jogador == 2:
                             print('Tá bom, vc ganhou ')
                             usuario +=1
                         elif jogador == 0:
                             print ('HÁÁÁÁ... GANHEIIIII')
                             cpu +=1            
                         
                                      
                 elif jogadaComputador == 2: 
                         if jogador == 2:
                             print('EMPATAMOS!!')
                             empates +=1
                         elif jogador == 0:
                             print('Tá bom, vc ganhou ')
                             usuario +=1
                         elif jogador == 1:
                                 print ('HÁÁÁÁ... GANHEIIIII')
                                 cpu +=1
                      
                                  
                
                 print ('O Computador escolheu {}'.format(acoes[jogadaComputador]))              
                 print ('O Jogador escolheu {}'.format(acoes[jogador]))             
                 print(f'Rodada {jogos}  de {qt_jogos}')
                 if jogos < qt_jogos:                    
                     print('Proxima rodada!!')
                 print('***'*20) 
             print(f'Foram {jogos} jogos feitos')
             print(f'{empates} empates')
             print(f'{cpu} Vitorias da maquina')
             print(f'{usuario} Vitorias do usuario')
       if cpu > usuario: 
              print('NINGUEM PODE VENCER A MAQUINA')
       elif usuario > cpu :
              print('ACHO QUE VC ME ROUBOU... IMPOSSIVEL GANHAR DE MIM')
       else:
              print('EMPATAMOS , ATÉ QUE VC JOGA BEM!')     
       print('***'*20)       
       new_game = int(input('Quer jogar novamente?\n [1]SIM\n [2]NÃO\n'))
       if new_game == 1:
           usuario = 0
           cpu = 0
           empates = 0
           jogos = 0
           qt_jogos=  int(input('Quantos jogos vamos jogar?? ')) 