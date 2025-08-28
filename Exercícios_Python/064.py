# Mundo 2 - Exercício 064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# Resolvido sem auxílio.

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

soma = 0
cont = 0
num = 0

while num != 999:
    num = int(input("Digite um número: "))
    if num != 999:
        soma += num
        cont += 1
    else:
        print(f"Você digitou {cont} números e a soma entre eles foi {soma}.")
        break
