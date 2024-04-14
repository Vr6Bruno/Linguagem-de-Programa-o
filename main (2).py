# Genérico

# Importação do TypeVar do módulo typing para definir tipos genéricos em Python
from typing import TypeVar

# Tipo genérico "T"
T = TypeVar('T')

## Define uma função que imprime qualquer objeto
def print_anything(x: object) -> None:
  
    # Imprime o valor de x
    print(x)

# Uso do código genérico
print_anything("Bom dia meu povo!!!")  # Saída: Bom dia meu povo!!!
# Uso do código genérico
print_anything("Desejo a todos um bom dia!")  # Saída: Desejo a todos um bom dia!
