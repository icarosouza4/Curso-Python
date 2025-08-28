# Mundo 3 - Exercício 074 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
# Resolvido sem auxílio.

from random import randint

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

sort = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))

print("Os números sorteados foram: ",end="")

for n in sort:
    print(f"{n} ",end="")

print(f"\nO maior valor sorteado foi {max(sort)}.")
print(f"E o menor valor sorteado foi {min(sort)}.")
