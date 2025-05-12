# Curso de Programação Orientada a Objetos (POO)

### Nível: Intermediário a Avançado

### Objetivo Geral:
Capacitar os alunos a compreenderem os princípios fundamentais da Programação Orientada a Objetos (POO) em Python e a aplicá-los na criação de sistemas de software bem estruturados, reutilizáveis e de fácil manutenção.

**Público-Alvo**: Iniciantes e programadores com conhecimento básico em Python que desejam aprofundar seus conhecimentos em POO.

### Pré-requisitos: 
- Lógica de Programação
- Conhecimento Básico em Alguma Linguagem (Java, C#, Python, etc.)

### Por: David Hadrianus - 2025

---------------------------------------------------------------------------------
# Aula 4 - Organização com Encapsulamento

## Encapsulamento (Definição):
O encapsulamento é uma técnica de programação que envolve a combinação de dados e métodos para criar classes que controlam o acesso aos seus membros internos.

## Protegendo seus Dados
**O problema do acesso direto aos atributos**
Em Python, por padrão, os atributos de uma classe são públicos e podem ser acessados e modificados diretamente de fora da classe:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Alice", 30)
print(pessoa.idade)  # Acesso direto ao atributo

pessoa.idade = -5  # Atribuição de valor inválido!
print(pessoa.idade)      # Saída: Android
```
Isso pode levar a inconsistências, já que uma pessoa não pode ter uma idade negativa. Portanto, é importante controlar o acesso para proteger os dados e garantir que alterações sejam feitas seguindo regras definidas pela classe.

**A importância do controle de acesso**
O encapsulamento permite que você restrinja o acesso direto aos dados, protegendo-os contra modificações indevidas e promovendo a integridade do estado do objeto. Além disso, facilita a manutenção e reutilização do código.

## Convenção de Nomes para Controle de Acesso
Python não possui modificadores de acesso como ``private`` ou ``protected`` de outras linguagens, mas usa convenções:

**Atributos públicos**: sem prefixo, acessíveis de qualquer lugar.

**Atributos protegidos**: prefixados com um sublinhado simples ``_atributo``. Indicam que o atributo é interno, e não deve ser acessado diretamente fora da classe, mas não impedem o acesso.

**Atributos privados**: prefixados com dois sublinhados ``__atributo``. Python aplica name mangling, que dificulta o acesso direto de fora da classe.
```python
class Car:
    def __init__(self):
        self.publico = "Público"
        self._protegido = "Protegido"
        self.__privado = "Privado"

car = Car()
print(car.publico)      # Acesso normal
print(car._protegido)   # Acesso possível, mas não recomendado
print(car.__privado)    # Erro: atributo não encontrado
```
**OBS**: Internamente, o atributo privado é renomeado para ``_Car__privado`` e pode ser acessado assim, mas isso não é recomendado.

## Getters e Setters (Propriedades)
Implementando métodos get e set para controlar o acesso
Para controlar o acesso e permitir validações, criamos métodos para obter (``get``) e modificar (``set``) os atributos:

```python
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
```
**Benefícios da validação e lógica adicional**
**Os getters e setters permitem**:

- Validar valores antes de atribuir.

- Proteger dados sensíveis.

- Controlar como os dados são expostos.

Exemplo prático (ContaBancaria)
```python
conta = ContaBancaria(100)
print(conta.get_saldo())  # 100

conta.set_saldo(200)
print(conta.get_saldo())  # 200

conta.set_saldo(-50)      # Saldo não pode ser negativo
print(conta.get_saldo())  # Continua 200
```
**OBS**: Os métodos get e set podem ser usados para implementar lógica adicional, como validação e controle de acesso. Isso permite que você defina regras de negócio complexas para manipular os dados da classe.

## Propriedades com Decoradores (@property, @setter)
**Sintaxe elegante para getters e setters**
Python oferece uma forma mais elegante e idiomática para criar propriedades usando decoradores:

```python
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
```
Agora o acesso é feito como um atributo comum, mas com controle:
```python
conta = ContaBancaria(100)
print(conta.saldo)  # 100

conta.saldo = 300
print(conta.saldo)  # 300

conta.saldo = -10   # Saldo não pode ser negativo
print(conta.saldo)  # 300
```
Exemplo prático (Círculo)
```python
class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor > 0:
            self._raio = valor
        else:
            print("Raio deve ser positivo")

    @property
    def area(self):
        import math
        return math.pi * (self._raio ** 2)

c = Circulo(5)
print(c.raio)   # 5
print(c.area)   # 78.53981633974483

c.raio = 10
print(c.area)   # 314.1592653589793

c.raio = -3     # Raio deve ser positivo
```
## Considerações Finais
- O encapsulamento é essencial para proteger os dados internos das classes e garantir que eles sejam manipulados de forma controlada.

- Em Python, o encapsulamento é mais uma convenção do que uma restrição rígida, mas seguir essas práticas melhora a qualidade e manutenção do código.

- Usar propriedades com @property e @setter torna o código mais limpo e Pythonico.

- Validar dados nas setters evita erros e garante integridade.

--------------------------------------------------------------------------

# Aula 5 - Herança: Reutilização e Extensibilidade de Código

## A Ideia de Reutilização

**Criando novas classes a partir de classes existentes**
Herança é um conceito fundamental da Programação Orientada a Objetos (POO) que permite criar uma nova classe (subclasse ou classe filha) baseada em uma classe já existente (superclasse ou classe pai). A subclasse herda atributos e métodos da superclasse, podendo reutilizá-los e estendê-los.

**Evite repetição de código**
Com herança, evitamos duplicar código comum a várias classes, e isso facilita a manutenção e evolução do sistema.

## Sintaxe da Herança
Para criar uma classe filha que herda de uma classe pai, basta colocar o nome da classe pai entre parênteses na definição da filha:

```python
class Pai:
    pass

class Filho(Pai):
    pass
```
## O Método super()
**Chamando métodos da classe pai**
O ``super()`` é uma função que retorna um objeto temporário da superclasse, permitindo chamar seus métodos dentro da subclasse, especialmente útil no método ``__init__`` para garantir que a inicialização da superclasse ocorra corretamente.

Importância no método ``__init__``
Ao sobrescrever o construtor (``__init__``) da subclasse, é importante chamar ``super().__init__()`` para inicializar os atributos da superclasse.

**Exemplo:**
```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # inicializa o nome na superclasse
        self.raca = raca
```
## Exemplo Detalhado: Hierarquia de Classes Animal
**Vamos modelar uma hierarquia simples:**

- Animal (superclasse)

- Mamifero (subclasse de Animal)

- Cachorro, Gato (subclasses de Mamifero)

- Peixe (subclasse de Animal)

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som genérico de animal")

class Mamifero(Animal):
    def __init__(self, nome, tem_pelo=True):
        super().__init__(nome)
        self.tem_pelo = tem_pelo

    def amamentar(self):
        print(f"{self.nome} está amamentando.")

class Cachorro(Mamifero):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        print("Au Au!")

class Gato(Mamifero):
    def fazer_som(self):
        print("Miau!")

class Peixe(Animal):
    def fazer_som(self):
        print("...")  # Peixes não fazem som audível para nós
```

## Sobrescrita de Métodos (Method Overriding)
**Redefinindo métodos da classe pai na classe filha**
A subclasse pode redefinir (sobrescrever) métodos da superclasse para alterar ou especializar o comportamento.

No exemplo acima, Cachorro e Gato sobrescrevem o método fazer_som() para emitir sons específicos.

## Adição de Novos Atributos e Métodos
Subclasses podem adicionar novos atributos e métodos que não existem na superclasse, estendendo sua funcionalidade.

No exemplo, Cachorro adiciona o atributo raca e o método amamentar vem da superclasse Mamifero.

## Hierarquia de Classes: Modelando Relacionamentos "É um tipo de"
**Herança modela o relacionamento "é um tipo de" (is-a).**

- Um Cachorro é um tipo de Mamifero.

- Um Mamifero é um tipo de Animal.

Isso permite tratar objetos de subclasses como objetos da superclasse, facilitando polimorfismo.

## Resumo:
meke a tabela com os conceitos da herança

| Conceito | Descrição |
| --- | --- |
| Herança | Relacionamento "é um tipo de" entre classes. |
| Subclasse | Classe que herda atributos e métodos da superclasse. |
| Superclasse | Classe que recebe herança. |
| Polimorfismo | Tratar objetos de subclasses como objetos da superclasse. |
| Sobrescrita de métodos | Redefinir métodos da superclasse na subclasse. |
| Adição de novos atributos e métodos | Adicionar novos atributos e métodos na subclasse. |
| Super() | Chamar métodos da superclasse dentro da subclasse. |

--------------------------------------------------------------

# Aula 6 - Polimorfismo: Uma Interface, Múltiplas Formas

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
