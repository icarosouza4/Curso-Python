# Mundo 2 - Exercício 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
# Resolvido sem auxílio.

from random import randint

Verde = "\033[32m"

print(f"{Verde}")

vitorias = 0
soma = 0

while True:
    computador = randint(0,1000)
    jogador = int(input("Digite um número: "))
    parimpar = " "
    while parimpar not in "PI":
        parimpar = input("Par ou ímpar? [P/I] ").upper()[0]
    print(f"Você escolheu {jogador} e o computador escolheu {computador}.")
    soma = jogador + computador
    if soma % 2 == 0:
        print(f"A soma entre {jogador} e {computador} é igual a {soma}. Ele é par.")
    else:
        print(f"A soma entre {jogador} e {computador} é igual a {soma}. Ele é ímpar.")
    if soma % 2 == 0 and parimpar == "P":
        print("Você ganhou!")
        vitorias += 1
    elif soma % 2 != 0 and parimpar == "I":
        print("Você ganhou!")
        vitorias += 1
    else:
        print("Você perdeu!")
        break

print(f"Você obteve {vitorias} vitórias consecutivas.")
