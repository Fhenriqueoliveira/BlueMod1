def somar(): 
    num1= float(input('Digite um numero: '))
    num2= float(input('Digite outro numero: '))
    soma = num1 + num2
    print(soma)

def area(a,b):
    terreno = a * b
    print( f'A area do terreno é {terreno}mts²')

larg= int(input('Digite a largura do terreno: '))    
comp= int(input('Digite o comprimento do terreno: '))    
area(larg,comp)
#==========================***********======================0

def soma(x,y):
    num = x * y
    return num
    print("teste")

print(soma(10,20))