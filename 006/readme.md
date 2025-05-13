# Aula 6 - Herança: Reutilização e Extensibilidade de Código

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
