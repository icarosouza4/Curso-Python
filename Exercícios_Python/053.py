# Mundo 2 - Exercício 053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Resolvido com auxílio.

Ciano = "\033[36m"

print(f"{Ciano}")

print("Vamos verificar se a frase é um palíndromo.")

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]

print(inverso)

if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
