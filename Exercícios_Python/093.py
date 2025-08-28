# Mundo 3 - Exercício 093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# Resolvido sem auxílio.

Ciano = "\033[36m"

print(f"{Ciano}")

jogador = {}
gols = []

jogador["Nome"] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador["Nome"]} jogou? "))

for c in range(partidas):
    gols.append(int(input(f"Quantos gols na partida {c+1}? ")))
    total = sum(gols)

jogador["Gols"] = gols
jogador["Total"] = total

print("-="*30)
print(jogador)
print("-="*30) 

for k,v in jogador.items():
    print(f"-> O campo {k} tem o valor {v}.")

print("-="*30)
print(f"O jogador {jogador["Nome"]} jogou {partidas} partidas.")

for g in range(partidas):
    print(f" -> Na partida {g+1}, ele fez {gols[g]} gols.")

print(f"Foi um total de {total} gols.")
