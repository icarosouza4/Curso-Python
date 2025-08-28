# Mundo 3 - Exercício 095 - Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# Resolvido com auxílio.

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

jogador = {}
gols = []
lista = []

while True:
    gols.clear()
    total = 0
    jogador["Nome"] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogador["Nome"]} jogou? "))
    for c in range(partidas):
        gols.append(int(input(f"Quantos gols na partida {c+1}? ")))
        total = sum(gols)
    jogador["Gols"] = gols
    jogador["Total"] = total
    lista.append(jogador.copy())
    while True:
        resp = str(input("Deseja continuar? [S/N]")).upper()
        if resp in "SN":
            break
        print("Resposta inválida. Tente novamente.")
    if resp == "N":
        break

print("-="*30)
print(f"Nº ", end = "")
for i in jogador.keys():
    print(f" {i:<15}", end = " ")

print()
print("-="*30)

for k,v in enumerate(lista):
    print(f"{k:>3}", end = "")
    for d in v.values():
        print(f"{str(d):<15}", end = "")
    print()

print("-="*30)

while True:
    opc = int(input("Mostrar as estatísticas de qual jogador? (999 para encerrar) "))
    if opc == 999:
        break
    if opc >= len(lista):
        print(f"Jogador {opc} não encontrado.")
    else:
        print(f" -- Estatísticas do jogador {lista[opc]["Nome"]} -- ")
        for i,g in enumerate(lista[opc]["Gols"]):
            print(f"No jogo {i+1} marcou {g} gols.")
    print("-="*30)
    
print("<< FIM >>")
