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
           return('VOCÊ NÃO PODE VOTAR AINDA')
        elif autorizacao == 2:
            print('SEU VOTO É OPCIONAL!')
        else:
            print('VOTO OBRIGATÓRIO!')        
        continua = 'S'
        pele= 0
        ronaldo= 0
        romario=0
        nulo=0
        branco=0
        result={'Pelé':pele,'Ronaldo':ronaldo,'Romario':romario,'Nulo':nulo,'Branco':branco}    
        while continua == 'S':
            usuario = int(input('Qual o seu voto: '))
            
            if usuario == 1:
                    pele +=1
                    continua =input('Nova votação? [S/N] ').upper()
                    
            elif usuario==2:
                    ronaldo +=1
                    continua =input('Nova votação? [S/N] ').upper()
                            
            elif usuario== 3:
                    romario +=1        
                    continua =input('Nova votação? [S/N] ').upper()
                    
            elif usuario== 4:
                    nulo +=1        
                    continua =input('Nova votação? [S/N] ').upper()
                    
            elif usuario== 5:
                    branco +=1        
                    continua =input('Nova votação? [S/N] ').upper()   
                 
        
        if ronaldo<pele>romario:
            if pele != ronaldo and pele != romario:
                result= {'Pelé':pele,'Ronaldo':ronaldo,'Romario':romario,'Nulo':nulo,'Branco':branco}
                return result.items(),(f'Péle foi o Vencedor da votação')
            else:
                return result.items(), 'Deu empate. Vamos precisar de segundo turno'    
        elif ronaldo > romario:
            if ronaldo != romario and ronaldo != pele:
                result= {'Ronaldo':ronaldo,'Pelé':pele,'Romario':romario,'Nulo':nulo,'Branco':branco}            
                return result.items(),(f'Ronaldo foi o Vencedor da votação')
            else:
                return result.items(),'Deu empate. Vamos precisar de segundo turno'    
        elif ronaldo != romario and romario != pele :
            result= {'Romario':romario,'Pelé':pele,'Ronaldo':ronaldo,'Nulo':nulo,'Branco':branco}    
            return result.items(),(f'Romario foi o Vencedor da votação')
        else:
            result= {'Pelé':pele,'Ronaldo':ronaldo,'Romario':romario,'Nulo':nulo,'Branco':branco}
            return result.items(),'Deu empate. Vamos precisar de segundo turno'

autoriza =( int(input('Qual o ano que vc nasceu: '))) 
idade=  autoriza_voto(autoriza)         
usuario=0
resultado_votacao = votacao(idade,usuario)
print(resultado_votacao)
#for pos,result in enumerate(resultado_votacao):
   

