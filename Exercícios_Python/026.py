# Mundo 1 - Exercício 026 - Faça um programa que leia uma frase pelo teclado e mostre:
# A) Quantas vezes aparece a letra "A".
# B) Em que posição ela aparece a primeira vez.
# C) Em que posição ela aparece a última vez.
# Resolvido sem auxílio.

Amarelo = "\033[33m"

print(f"{Amarelo}")

frase = str(input("Digite uma frase: ")).strip()

print(f"A letra A aparece {frase.upper().count("A")} vezes na frase.")
print(f"A primeira letra A aparece na posição {frase.upper().find("A") + 1}.")
print(f"A última letra A aparece na posição {frase.upper().rfind("A") + 1}.")
