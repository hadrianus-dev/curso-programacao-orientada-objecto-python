class Pai:
    pass

class Filha(Pai):
    pass

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som genérico de animal")

class Mamifero(Animal):
    def __init__(self, nome, tem_pelo=True):
        super().__init__(nome)
        self.tem_pelo = tem_pelo

    def fazer_som(self):
        print("Som genérico de mamifero")

class Cachorro(Mamifero):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        print("Au au")

class Gato(Mamifero):
    def fazer_som(self):
        print("Miau!")

class Peixe(Animal):
    def fazer_som(self):
        print("...")  # Peixes não fazem som audível para nós

gato = Gato("Felix")
gato.fazer_som()
