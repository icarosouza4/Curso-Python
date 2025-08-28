# Mundo 1 - Exercício 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Resolvido com auxílio.

Azul = "\033[34m"

print(f"{Azul}")

num = int(input("Digite um número de 0 a 999: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"Analisando o número {num}, temos:")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
