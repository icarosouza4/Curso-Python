# Mundo 2 - Exercício 048 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# Resolvido com auxílio.

Vermelho = "\033[31m"

print(f"{Vermelho}")

s = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1

print(f"A soma de todos os {cont} valores é {s}.")
