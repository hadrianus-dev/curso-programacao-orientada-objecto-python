# Aula 8: Interfaces: Definindo e Implementando Interfaces em Python

## O que é uma Interface?
Uma interface em Python é uma forma de definir um conjunto de metodos que devem ser implementados por uma classe.

## Como criar uma Interface em Python?
Para criar uma interface em Python, vocé pode usar a classe ABC (Abstract Base Class) do módulo abc.

Com o módulo abc (Abstract Base Classes), você pode criar uma classe abstrata que define métodos e propriedades que todas as subclasses devem implementar obrigatoriamente. Isso funciona como uma interface formal, impedindo a instanciação direta da classe abstrata e forçando a implementação dos métodos definidos.

Exemplo:

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
```
## Usando polimorfismo por interface

```python
def imprimir_detalhes(formas):
    for forma in formas:
        print(f"Área: {forma.area():.2f}, Perímetro: {forma.perimetro():.2f}")

formas = [Retangulo(3, 4), Circulo(5)]
imprimir_detalhes(formas)
```
## Propriedades abstratas
Além de métodos, você pode definir propriedades abstratas para garantir que as subclasses implementem atributos ou propriedades específicas:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def som(self):
        pass

class Cachorro(Animal):
    @property
    def som(self):
        return "Au Au"
```