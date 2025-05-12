class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"Ola, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa = Pessoa("Alice", -30)
pessoa.apresentacao()

class AnyClass:
    def __init__(self):
        self.public_attribute = 1
        self._protected_attribute = 2
        self.__private_attribute = 3

anyobject = AnyClass()
print(f'atributo publico: {anyobject.public_attribute}')
print(f'atributo protegido: {anyobject._protected_attribute}')
# print(f'atributo privado: {anyobject.__private_attribute}')

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo")

conta = ContaBancaria(1000)
print(conta.get_saldo())
conta.set_saldo(200)
print(conta.get_saldo())

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo")
print('------------------------------------------------------')
conta = ContaBancaria(1000)
print(conta.saldo)
conta.saldo =  200
print(conta.saldo)
