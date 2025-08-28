# Mundo 2 - Exercício 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Resolvido sem auxílio.

from datetime import date

ano = date.today().year
maior = 0
menor = 0

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

for c in range(1, 8):
    nascimento = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(c)))
    idade = ano - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print("Ao todo tivemos {} pessoas maiores de idade.".format(maior))
print("E também tivemos {} pessoas menores de idade.".format(menor))
