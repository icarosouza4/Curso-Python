# Mundo 3 - Exercício 113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também a função leiaFloat() com a mesma funcionalidade.
# Resolvido com auxílio.

from Meu_pacote import Dados

numint = Dados.leiaInt("Digite um número inteiro: ")
numreal = Dados.leiaFloat("Digite um número real: ")

print(f"\033[95mO valor inteiro digitado foi {numint} e o valor real digitado foi {numreal}.\033[0m")
