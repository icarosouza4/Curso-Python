# Mundo 2 - Exercício 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# Resolvido com auxílio.

Azul = "\033[34m"

print(f"{Azul}")

pa = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

for c in range(pa, pa + 10 * r, r):
    print(c, end=" ")
