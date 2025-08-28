# Mundo 3 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# Resolvido com auxílio.

from random import randint
from time import sleep
from operator import itemgetter

Azul = "\033[34m"

print(f"{Azul}")

jogo = {"Jogador 1": randint(1,6),
        "Jogador 2": randint(1,6),
        "Jogador 3": randint(1,6),
        "Jogador 4": randint(1,6)}
ranking = []

print("Valores sorteados: ")

for k,v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("-="*30)
print("  == RANKING DOS JOGADORES ==")

for i,v in enumerate(ranking):
    print(f"   {i+1}º lugar: {v[0]} com {v[1]}.")
    sleep(1)
    