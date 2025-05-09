
# Aula 2: Desvendando Classes, Objetos e Métodos

## A Essência das Classes e Objetos:

Analogia do Mundo Real: Pense em uma planta (a classe) e várias mudas dessa planta (os objetos). A planta define as características (atributos, como cor das folhas, tipo de flor) e comportamentos (métodos, como crescer, florescer). Cada muda é uma instância concreta dessa planta, com seus próprios valores para essas características.

**Classes como Moldes**: Uma classe é como um molde ou um projeto para criar objetos. Ela define a estrutura e o comportamento que os objetos dessa classe terão.

**Objetos como Instâncias**: Um objeto é uma instância específica de uma classe. É a materialização do projeto definido pela classe.

## Criando sua Primeira Classe:

Em Python, usamos a palavra-chave ***class*** seguida pelo nome da classe (por convenção, com a primeira letra maiúscula) e dois pontos ```(:)```. O corpo da classe (onde definimos seus atributos e métodos) é indentado.

Sintaxe da definição de classe ```(class)```.
```python
class MinhaPrimeiraClasse:
    # O corpo da classe vem aqui
    pass  # 'pass' é usado quando você não quer colocar nada no corpo da classe ainda
```

Exemplo de uma classe simples, sem atributos ou métodos:
```python
class Pessoa:
    pass
```
## Atributos (Características)
Atributos são as características que um objeto de uma classe terá. Podemos definir atributos diretamente dentro da classe ou, mais comumente, dentro de um método especial chamado ```__init__.```

```python
class Exemplo:
    atributo_da_classe = "Este é um atributo da classe"

# criando objeto a partir da classe, e acessando o atributo da classe
objeto = Exemplo()
print(objeto.atributo_da_classe)  # Saída: Este é um atributo da classe

outro_objeto = Exemplo()
print(outro_objeto.atributo_da_classe) # Saída: Este é um atributo da classe
```
Outra forma de definir atributos:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# criando objeto a partir da classe
pessoa1 = Pessoa("Joaquim", 30)
# acessando os atributos do objeto
print(pessoa1.nome)  # Saída: Joaquim
print(pessoa1.idade) # Saída: 30
```

O método ```__init__``` (construtor) e o ```self```

O método ```__init__``` é um método especial que é chamado automaticamente quando um novo objeto da classe é criado (instanciado). Ele é usado para inicializar os atributos do objeto.

O primeiro parâmetro de ```__init__``` (e de todos os métodos de instância em Python) é sempre ```self.``` ```self``` é uma convenção e representa a própria instância do objeto que está sendo criado ou manipulado. Usamos ```self``` para acessar os atributos e outros métodos do objeto dentro da classe.


## Métodos (Ações/Comportamentos)

**Definindo métodos dentro da classe**

A sintaxe para definir métodos dentro de uma classe é a mesma de definir funções em Python, com a diferença crucial de que o primeiro parâmetro deve ser ```self.```

Exemplo Prático (adicionando métodos a classe ```Pessoa```):

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} está falando...")

    def comer(self):
        print(f"{self.nome} esta comendo...")

# criando objeto a partir da classe
pessoa1 = Pessoa("Antonio", 30)
# acessando os metodos do objeto
print(pessoa1.falar())  # Saída: Joaquim
print(pessoa1.comer()) # Saída: 30
```

## Instanciando Objetos

**Criando instâncias de uma classe**

Para criar uma instância de uma classe, você chama o nome da classe como se fosse uma função, passando os argumentos necessários para o método ```__init__``` (se houver).

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando instâncias da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

print(pessoa1)  # Saída: <__main__.Pessoa object at 0x...> (endereço de memória do objeto)
print(pessoa2)  # Saída: <__main__.Pessoa object at 0x...> (outro endereço de memória)
```

Cada vez que você chama Pessoa(...), um novo objeto Pessoa é criado com seus próprios atributos nome e idade. pessoa1 e pessoa2 são variáveis que referenciam esses objetos distintos na memória.

Acessando atributos com a notação de ponto (.)

Para acessar os atributos de um objeto, usamos a notação de ponto (.) seguida pelo nome do atributo.

```python
print(pessoa1.nome)  # Saída: Alice
print(pessoa2.idade) # Saída: 25
```
**Chamando métodos de instância**

Da mesma forma, usamos a notação de ponto para chamar os métodos de um objeto.

```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

meu_livro = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
meu_livro.exibir_info()  # Saída: Título: O Pequeno Príncipe, Autor: Antoine de Saint-Exupéry
```
Ao chamar ```meu_livro.exibir_info()```, o método ```exibir_info``` associado ao objeto ```meu_livro``` é executado, e o ```self``` dentro do método se refere a essa instância específica do livro, permitindo que ele acesse seus próprios atributos ```titulo``` e ```autor```.
