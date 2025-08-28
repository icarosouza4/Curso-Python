# Mundo 1 - Exercício 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
# Resolvido sem auxílio.

Branco_brilhante = "\033[97m"

print(f"{Branco_brilhante}")

num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
