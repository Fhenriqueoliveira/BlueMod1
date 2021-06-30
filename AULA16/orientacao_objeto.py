class Mamifero():
    #def __init__(self) -> None:
     #   pass
#criando o método construtor, ele vai seguir para passar todos os atributos para o objeto que estou criando.
    def __init__(self,nome,pelo,cor,tamanho,idade):
        self.nome = nome
        self.pelo = pelo
        self.cor = cor
        self.tamanho = tamanho
        self.idade = idade

    def crescer(self):
        self.idade +=1    
    def locomover(self):
        print('Ele esta andando')
    def comer(self):
        self.tamanho = 'grande'        


cachorro=Mamifero('Bart','curto','cinza','medio',1) 
cachorro.crescer()
cachorro.locomover()
cachorro.comer()
print(vars(cachorro))       