# Mundo 1 - Exercício 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# A) O nome com todas as letras maiúsculas e minúsculas.
# B) Quantas letras ao todo (sem considerar espaços).
# C) Quantas letras tem o primeiro nome.
# Resolvido sem auxílio.

Vermelho = "\033[31m"

print(f"{Vermelho}")

nome = input("Digite seu nome: ")
nome_separado = nome.split()

print(f"O nome em letras maiúsculas: {nome.upper()}.")
print(f"O nome em letras minúsculas: {nome.lower()}.")
print(f"O nome possui {len(nome) - nome.count(" ")} letras.")
print(f"O primeiro nome é {nome_separado[0]} e possui {len(nome_separado[0])} letras.")
