# Mundo 2 - Exercício 047 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# Resolvido sem auxílio.

Preto = "\033[30m"

print(f"{Preto}")

for n in range(1, 51):
    print(" ", end = "")
    if n % 2 == 0:
        print(n, end = "")

print(" FIM")
