# Aula 4 - Métodos Estáticos

Já os **métodos estáticos** são associados à própria classe, não a uma instância, e não podem acessar diretamente os atributos de instância, necessitando de uma instância para serem chamados.

## MÉTODOS ESTÁTICOS

### Métodos Estáticos: Propósito e quando usar
**Propósito**: Métodos estáticos são métodos que pertencem à classe, mas não precisam de uma instância da classe para serem chamados. Eles não têm acesso direto aos atributos de uma instância (não recebem o parâmetro self implicitamente).

**Quando usar**: Métodos estáticos são úteis quando você tem uma função que está logicamente relacionada à classe, mas não depende do estado de nenhum objeto específico dessa classe. 

**Eles são frequentemente usados para:**
- Criar funções utilitárias relacionadas à classe.
- Implementar operações que se aplicam à classe como um todo, em vez de a uma instância específica.
- Agrupar logicamente funções dentro do escopo de uma classe para melhor organização do código.

**Usando A anotação** ```@staticmethod```

Para definir um método estático em Python, usamos o decorador ```@staticmethod``` antes da definição do método. Um decorador é uma forma de modificar o comportamento de uma função ou método.

```python
class MinhaClasse:
    @staticmethod
    def metodo_estatico():
        print("Este é um método estático.")

# Chamando o método estático (não precisamos de uma instância)
MinhaClasse.metodo_estatico()

# Também podemos chamar através de uma instância (menos comum)
objeto = MinhaClasse()
objeto.metodo_estatico()
```
Perceba que ```metodo_estatico``` não tem o parâmetro ``self``

**Exemplo Prático (Geometria)**
Vamos criar uma classe Geometria com um método estático para calcular a área de um retângulo, sem precisar de um objeto Geometria específico

```python
class Geometria:
    @staticmethod
    def area_retangulo(base, altura):
        return base * altura

    @staticmethod
    def area_triangulo(base, altura):
        return (base * altura) / 2

print(Geometria.area_retangulo(5, 3))    # Saída: 15
print(Geometria.area_triangulo(5, 3))    # Saída: 7.5


# Chamando o método estático diretamente da classe
area = Geometria.area_retangulo(5, 10)
print(f"A área do retângulo é: {area}")
```
Neste caso, a função de calcular a área do retângulo está logicamente relacionada à geometria, mas não depende das propriedades de um objeto geométrico específico.

**Exemplo Integrado: Classe Livro com atributos, métodos de instância e um método estático**

Vamos expandir a classe Livro para incluir atributos, métodos de instância e um método estático para verificar se um ISBN tem o formato correto (simplificado).

```python
class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = int(ano_publicacao)
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self.titulo} | {self.autor} | {self.ano_publicacao} | {self.disponivel}'

    @property
    def disponivel(self):
        return '☐' if self._disponivel else '☒'

    def emprestar_livro(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro.ano_publicacao == ano and livro._disponivel:
                livros_disponiveis.append(livro)
        return livros_disponiveis

# Exemplo de uso:
livro1 = Livro('Python Básico', 'João Silva', 2024)
livro2 = Livro('Algoritmos', 'Maria Souza', 2023)

livro1.emprestar_livro()
disponiveis_2023 = Livro.verificar_disponibilidade(2023)
for livro in disponiveis_2023:
    print(livro)
```
Neste exemplo:

- ``emprestar_livro`` é um método de instância, pois modifica o estado do objeto.

- ``verificar_disponibilidade`` é um método estático, pois apenas consulta informações e não depende de uma instância específica.

## Resumo: Diferenças entre Métodos de Instância e Estáticos

| Característica | Métodos de Instância | Métodos Estáticos |
| --- | --- | --- |
| Recebe self | Sim | Não |
| Acesso a atributos | Da instância (e da classe) | Não |
| Uso do decorador | Não (exceto ``@property`` etc.) | Sim, ``@staticmethod`` |
| Quando usar | Precisa do estado do objeto | Função utilitária relacionada |
| Chamada | Instância ou classe | Classe ou instância |

Métodos estáticos são ferramentas poderosas para organizar funções relacionadas à classe, mas que não dependem do estado de objetos específicos. Use-os para manter seu código mais limpo e modular.

