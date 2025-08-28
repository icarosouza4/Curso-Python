# Mundo 1 - Exercício 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
# Resolvido sem auxílio.

Magenta = "\033[35m"

print(f"{Magenta}")

cidade = str(input("Digite o nome da cidade: ")).strip()

print(cidade[:5].upper() == "SANTO")
