class Pessoa():
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def mostrar_dados(self):
        print(f'O {pessoa.nome} {pessoa.sobrenome} tem {pessoa.idade}')



pessoa= Pessoa('Fabio','Oliveira',34)
pessoa.mostrar_dados()
