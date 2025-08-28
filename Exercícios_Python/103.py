# Mundo 3 - Exercício 103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
# Resolvido com auxílio.

Ciano = "\033[36m"

print(f"{Ciano}")

def ficha(j = "<desconhecido>",g = 0):
    estatística = print(f"O jogador {j} fez {g} gol(s) no campeonato.")
    return estatística

jogador = str(input("Nome do Jogador: "))
gols = str(input("Número de gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador.strip() == "":
    ficha(g = gols)
else:
    ficha(jogador, gols)
