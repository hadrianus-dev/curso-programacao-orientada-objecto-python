class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} está falando...")

    def comer(self):
        print(f"{self.nome} esta comendo...")

    def maior_de_idade(self):
        return 'Maior de Idade' if self.idade >= 18 else 'Menor de Idade'

pessoa1 = Pessoa("Antonio", 30)
pessoa1.falar()
pessoa1.comer()
print(pessoa1.maior_de_idade())
print('------------------------------------------')
pessoa2 = Pessoa("Maria", 15)
pessoa2.falar()
pessoa2.comer()
print(pessoa2.maior_de_idade())
print('------------------------------------------')

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente.")

# Criando instâncias da classe ContaBancaria
conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob")

# Chamando métodos de instância
conta1.depositar(500)   # 'self' é 'conta1'
conta2.sacar(100)     # 'self' é 'conta2' (saldo inicial é 0)
print('------------------------------------------------------')
conta2.depositar(1000) 
conta2.sacar(450) 