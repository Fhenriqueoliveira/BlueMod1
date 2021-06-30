def autoriza_voto(dt_nasc):
    from datetime import date
   
    data_atual= date.today().year
    idade = data_atual - dt_nasc
    if 18 <= idade <=65:
        return 1
    elif idade >= 16 or idade > 65:
        return 2
    else:
        return 0

def votacao(autorizacao,usuario):
        if autorizacao == 0:
           return
        elif autorizacao == 2:
            print('SEU VOTO É OPCIONAL!')
            print('='*70) 
        else:
            print('VOTO OBRIGATÓRIO!') 
            print('='*70) 
        continua = 'S'    
        print( 'Suas opções são:\n Pelé [1]\n Ronaldo [2]\n Romario[3]\n Nulo[4]\n Branco[5]')
        print('='*70)           
        pele= 0
        ronaldo= 0
        romario=0
        nulo=0
        branco=0
        vencedor = ''
        result={'Resultado':vencedor,'Pelé':pele,'Ronaldo':ronaldo,'Romario':romario,'Nulo':nulo,'Branco':branco}    
        while continua == 'S':
            usuario = int(input('Qual o seu voto: '))
            print('='*70)
            if usuario == 1:
                    pele +=1
                    continua =input('Nova votação? [S/N] ').upper()  
                    print( 'Suas opções são:\n Pelé [1]\n Ronaldo [2]\n Romario[3]\n Nulo[4]\n Branco[5]')
                    print('='*70)
                    
                    
            elif usuario==2:
                    ronaldo +=1
                    continua =input('Nova votação? [S/N] ').upper()  
                    print( 'Suas opções são:\n Pelé [1]\n Ronaldo [2]\n Romario[3]\n Nulo[4]\n Branco[5]')
                    print('='*70)
                    
                            
            elif usuario== 3:
                    romario +=1        
                    continua =input('Nova votação? [S/N] ').upper()  
                    print( 'Suas opções são:\n Pelé [1]\n Ronaldo [2]\n Romario[3]\n Nulo[4]\n Branco[5]')
                    print('='*70)
                    
                    
            elif usuario== 4:
                    nulo +=1        
                    continua =input('Nova votação? [S/N] ').upper()  
                    print( 'Suas opções são:\n Pelé [1]\n Ronaldo [2]\n Romario[3]\n Nulo[4]\n Branco[5]')
                    print('='*70)
                    
                    
            elif usuario== 5:
                    branco +=1   
                    continua =input('Nova votação? [S/N] ').upper()       
                    print( 'Suas opções são:\n Pelé [1]\n Ronaldo [2]\n Romario[3]\n Nulo[4]\n Branco[5]')
                    print('='*70)
                        
        
        if ronaldo<pele>romario:
            vencedor = ' Pelé foi o campeão!'
            result= {'Resultado':vencedor,'Pelé':pele,'Ronaldo':ronaldo,'Romario':romario,'Nulo':nulo,'Branco':branco}
            print('='*70)
            return result.items()
        elif ronaldo > romario:
            vencedor = ' Ronaldo foi o campeão!'
            result= {'Resultado':vencedor,'Pelé':pele,'Ronaldo':ronaldo,'Romario':romario,'Nulo':nulo,'Branco':branco}           
            print('='*70)
            return result.items()
        else:
            vencedor = ' Romario foi o campeão!'
            result= {'Resultado':vencedor,'Pelé':pele,'Ronaldo':ronaldo,'Romario':romario,'Nulo':nulo,'Branco':branco}  
            print('='*70)
            return result.items()

print('='*70)
print()
print('****Bem vindo a votação do melhor goleador do Brasil****')
print()
print('='*70)
autoriza =( int(input('Qual o ano que vc nasceu: ')))
print('='*70) 
idade=  autoriza_voto(autoriza)         
usuario=0
if idade == 0:
    print('VOCE NÃO PODE VOTAR!')
else:
    resultado_votacao = votacao(idade,usuario)
    for key,value in resultado_votacao:
        print(key ,value)