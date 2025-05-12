import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

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
print('------------------------------------------------------')

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
    
    def devolver_livro(self):
        self._disponivel = True

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro.ano_publicacao == ano and livro._disponivel:
                livros_disponiveis.append(livro)
        return livros_disponiveis

# Exemplo de uso:
livro1 = Livro('Python Básico', 'João Silva', 2024)
livro1 = Livro('Python Avancado', 'Silveira Nunda', 2024)
livro2 = Livro('Algoritmos', 'Maria Souza', 2023)

livro1.emprestar_livro()
livro1.devolver_livro()
disponiveis_2024 = Livro.verificar_disponibilidade(2024)
for livro in disponiveis_2024:
    print(livro)
