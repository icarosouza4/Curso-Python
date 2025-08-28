# Mundo 2 - Exercício 061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# Resolvido sem auxílio.

Azul = "\033[34m"

print(f"{Azul}")

primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo} -", end=" ")
    termo += razao
    cont += 1
