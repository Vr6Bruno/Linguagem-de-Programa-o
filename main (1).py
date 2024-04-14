# Reflexão

# Define a classe Pessoa
class Pessoa:
    # Define o método de inicialização da classe Pessoa
    def __init__(self, nome, idade, cidade):
        # Cria atributos para a instância
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    # Define um método para obter informações da instância
    def get_info(self):
        # Retorna um dicionário 
        return vars(self)

# Cria uma instância da classe Pessoa 
pessoa = Pessoa("João", 30, "São Paulo")

# Chama o método get_info da instância pessoa e imprime o resultado
print(pessoa.get_info())
