# Mundo 2 - Exercício 038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# A) O primeiro valor é maior
# B) O segundo valor é maior
# C) Não existe valor maior, os dois são iguais
# Resolvido sem auxílio.

Amarelo = "\033[33m"

print(f"{Amarelo}")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print("O primeiro número é maior.")
elif n2 > n1:
    print("O segundo número é maior.")
else:
    print("Os números são iguais.")
