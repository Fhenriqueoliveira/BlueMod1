#Crie uma classe chamada Conta para simular as operações de
#uma conta corrente. Sua classe deverá ter os atributos Titular e
#Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
#Conta e teste os atributos e métodos implementados.

class Conta():
    def __init__(self,titulo,saldo):
        self.titulo = titulo
        self.saldo = saldo

    def Sacar(self,valor_saque):
        self.saldo - valor_saque    
        print(f'O saldo atual é {self.saldo}')
    def Depositar(self,valor_dep):
        self.saldo + valor_dep
        print(f'O saldo atual é {self.saldo}')
operacao =Conta('Fabio Henrique de Oliveira',67.345)
operacao.Depositar(6666)
