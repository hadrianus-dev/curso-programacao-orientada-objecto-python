from typing import List
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        import math
        return math.pi * self.raio ** 2
    
    def perimetro(self):
        pass

def calcular_areas(formas: List[object]):
    for forma in formas:
        try:
            print(f"{str(forma).ljust(20)} -> Área: {forma.area()}")
        except Exception as e:
            print(f"⚠️ Erro: {type(forma).__name__} não implementa um método 'area()'")

formas = [Retangulo(3, 4), Circulo(5), 'Texto']
calcular_areas(formas)  # Área: 12 / Área: 78.5398...
