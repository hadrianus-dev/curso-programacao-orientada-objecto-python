# Sintaxe da definição de classe
class MinhaPrimeiraClasse:
    # O corpo da classe vem aqui
    pass  # 'pass' é usado quando você não quer colocar nada no corpo da classe ainda
# Atributos (Características)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
# Métodos (Ações/Comportamentos)
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_info(self):
        print(f"Título do Livro: {self.titulo}, Autor do Livro: {self.autor}")

    def alterar_informacao(self, novo_titulo, novo_autor):
        self.titulo = novo_titulo
        self.autor = novo_autor

# Instanciando Objetos
livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
livro1.exibir_info()

livro1.alterar_informacao("O Senhor dos Aneis", "J.R.R Tolkien")
livro1.exibir_info()

livro2 = Livro("O Hobbit", "J.R.R Tolkien")
livro2.exibir_info()

print(livro1 == livro2) # retorna False
print(livro1, livro2) # istor retorna o endereço de memória
