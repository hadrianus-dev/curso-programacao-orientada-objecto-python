from typing import List
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

class Cachorro:
    def som(self):
        print("Au Au!")

class Gato:
    def som(self):
        print("Miau!")

def emitir_som(animal):
    animal.som()

cachorro = Cachorro()
gato = Gato()

emitir_som(cachorro)
emitir_som(gato)

print('----------------------------------')

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        import math
        return math.pi * self.raio ** 2

def calcular_areas(formas: List[object]):
    for forma in formas:
        try:
            print(f"{str(forma).ljust(20)} -> Área: {forma.area()}")
        except Exception as e:
            print(f"⚠️ Erro: {type(forma).__name__} não implementa um método 'area()'")

formas = [Retangulo(3, 4), Circulo(5), 'Texto']
calcular_areas(formas)  # Área: 12 / Área: 78.5398...
