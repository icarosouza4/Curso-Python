# Mundo 2 - Exercício 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
# Resolvido sem auxílio.

Branco_brilhante = "\033[97m"

print(f"{Branco_brilhante}")

n = 0
while True:
    n = int(input("\nQuer ver a tabuada de qual valor? (digite um número negativo para parar) "))
    print("")
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {n*c}")

print("Programa encerrado.")
