# Mundo 3 - Exercício 088 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão sorteados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# Resolvido sem auxílio.

from random import randint
from time import sleep

Vermelho = "\033[31m"

print(f"{Vermelho}")

listanum = []
totaldejogos = []

quantidade = int(input("Quantos jogos serão sorteados? "))

tot = 1

while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in listanum:
            listanum.append(num)
            cont += 1
        if cont >= 6:
            break
    listanum.sort()
    totaldejogos.append(listanum[:])
    listanum.clear()
    tot += 1

for i,l in enumerate(totaldejogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
