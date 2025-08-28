# Mundo 2 - Exercício 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# Resolvido sem auxílio.

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

for c in range(1,7):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("O maior peso lido foi de {} kg.".format(maior))
print("O menor peso lido foi de {} kg.".format(menor))
