# Mundo 1 - Exercício 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Resolvido sem auxílio.

from math import trunc

Azul = "\033[34m"

print(f"{Azul}")

num = float(input("Digite um número: "))

print(f"O número digitado foi {num} e a sua porção inteira é {trunc(num)}.")
