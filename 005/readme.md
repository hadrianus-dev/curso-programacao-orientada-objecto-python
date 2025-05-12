# Aula 5 - Organização com Encapsulamento

## Encapsulamento (Definição):
O encapsulamento é uma técnica de programação orientada a objetos que envolve a combinação de dados e métodos para criar classes que controlam o acesso aos seus membros internos.

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
