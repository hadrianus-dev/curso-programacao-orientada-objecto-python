# Aula 7 - Polimorfismo: Uma Interface, Múltiplas Formas

## A Essência do Polimorfismo

Polimorfismo permite que objetos de diferentes classes respondam ao mesmo método de maneiras distintas, baseando-se em suas implementações específicas. Em Python, isso é possível graças à tipagem dinâmica e ao Duck Typing.

**Exemplo Básico:**
```python
class Cachorro:
    def som(self):
        return "Au Au!"

class Gato:
    def som(self):
        return "Miau!"

def emitir_som(animal):
    print(animal.som())

cachorro = Cachorro()
gato = Gato()

emitir_som(cachorro)  # Au Au!
emitir_som(gato)      # Miau!
```
## Duck Typing em Python
O Duck Typing ("se anda como um pato e faz som de pato, então é um pato") define que o Python não verifica o tipo do objeto, mas sim se ele possui o método ou atributo necessário. O foco está no comportamento, não na classe.

```python
class Carro:
    def ligar(self):
        print("Vrum Vrum!")

class Ventilador:
    def ligar(self):
        print("Zzzzzzz...")

def usar_dispositivo(dispositivo):
    dispositivo.ligar()

carro = Carro()
ventilador = Ventilador()

usar_dispositivo(carro)      # Vrum Vrum!
usar_dispositivo(ventilador) # Zzzzzzz...
```

## Polimorfismo por Herança
Quando classes filhas sobrescrevem métodos da classe pai, garantindo comportamentos específicos:

```python
class Animal:
    def fazer_som(self):
        pass

class Leao(Animal):
    def fazer_som(self):
        return "Roar!"

class Passaro(Animal):
    def fazer_som(self):
        return "Piu piu!"

def barulho_floresta(animais):
    for animal in animais:
        print(animal.fazer_som())

animais = [Leao(), Passaro()]
barulho_floresta(animais)  # Roar! / Piu piu!
```
## Polimorfismo por Interface (Implícito)
Em Python, não há interfaces formais, mas classes podem implementar métodos com o mesmo nome sem herança, permitindo polimorfismo implícito:

```python
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

def calcular_areas(formas):
    for forma in formas:
        print(f"Área: {forma.area()}")

formas = [Retangulo(3, 4), Circulo(5)]
calcular_areas(formas)  # Área: 12 / Área: 78.5398...
```
## Benefícios do Polimorfismo

| Benefício | Descrição |
|Código genérico|Funções podem trabalhar com qualquer objeto que implemente os métodos necessários.|
|Extensibilidade|Adicionar novas classes não requer alterar funções existentes.|
|Manutenção simplificada|Lógica centralizada em interfaces comuns.|

## Exercícios Práticos

**Exercício 1: Função Polimórfica para Formas Geométricas**
Crie uma função ``calcular_perimetro`` que aceite objetos de diferentes classes (como ``Quadrado``, ``Triangulo``) que tenham um método perimetro().
```python
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return 3 * self.lado

def calcular_perimetro(formas):
    for forma in formas:
        print(f"Perímetro: {forma.perimetro()}")

formas = [Quadrado(5), TrianguloEquilatero(4)]
calcular_perimetro(formas)  # Perímetro: 20 / Perímetro: 12
```
**Exercício 2: Sistema de Pagamento**
Implemente classes ``CartaoCredito``, ``Boleto``, e ``Pix``, cada uma com um método ``processar_pagamento(valor)``. Crie uma função ``efetuar_pagamento`` que aceite qualquer método de pagamento.

```python
class CartaoCredito:
    def processar_pagamento(self, valor):
        print(f"Pagamento de R${valor} via cartão de crédito.")

class Boleto:
    def processar_pagamento(self, valor):
        print(f"Gerando boleto de R${valor}.")

def efetuar_pagamento(metodo, valor):
    metodo.processar_pagamento(valor)

efetuar_pagamento(CartaoCredito(), 100)  # Pagamento de R$100 via cartão...
efetuar_pagamento(Boleto(), 50)         # Gerando boleto de R$50.
```
