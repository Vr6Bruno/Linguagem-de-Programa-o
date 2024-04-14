# Orientado a Objetos

# Define a classe Animal
class Animal:
    # Define o método de inicialização da classe Animal
    def __init__(self, nome):
        # Cria um atributo 
        self.nome = nome

    # Define um método fazer_som 
    def fazer_som(self):
        raise NotImplementedError("Método abstrato")

# Define a classe Cachorro 
class Cachorro(Animal):
    # Implementa o método fazer_som da classe Animal
    def fazer_som(self):
        return "Au Au!"

# Define a classe Gato 
class Gato(Animal):
    # Implementa o método fazer_som da classe Animal 
    def fazer_som(self):
        return "Miau!"

# Cria uma lista de animais 
animais = [Cachorro("Rex"), Gato("Whiskers")]

# Itera sobre a lista de animais
for animal in animais:
    # Imprime o nome do animal seguido pelo som que ele faz
    print(f"{animal.nome}: {animal.fazer_som()}")
