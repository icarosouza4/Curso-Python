# Mundo 1 - Exercício 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Resolvido sem auxílio.

Vermelho = "\033[31m"

print(f"{Vermelho}")

r1 = float(input("Digite o comprimento primeira reta: "))
r2 = float(input("Digite o comprimento segunda reta: "))
r3 = float(input("Digite o comprimento terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
