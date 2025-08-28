# Mundo 2 - Exercício 066 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# Resolvido sem auxílio.

Branco_brilhante = "\033[97m"

print(f"{Branco_brilhante}")

n = 0
s = 0
c = 0

while True:
    n = int(input("Digite um número inteiro (999 para parar): "))
    if n == 999:
        break
    s += n
    c += 1

print(f"\nVocê digitou {c} números e a soma entre eles foi {s}.")
