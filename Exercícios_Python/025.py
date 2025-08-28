# Mundo 1 - Exercício 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# Resolvido sem auxílio.

Magenta = "\033[35m"

print(f"{Magenta}")

nome = str(input("Digite seu nome: ")).strip()

print(f"Seu nome tem Silva? {"SILVA" in nome.upper()}.")
