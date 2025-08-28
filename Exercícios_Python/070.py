# Mundo 2 - Exercício 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
# Resolvido com auxílio.

Amarelo = "\033[33m"

print(f"{Amarelo}")

total = totmil = menor = cont = 0
barato = ""

while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()
    if resp == "N":
        break

print(f"Ao todo, tudo custou {total:.2f}.")

if totmil == 0:
    print(f"Com nenhum produto custando mais de R$1000,00.")
else: 
    print(f"Com {totmil} produto(s) custando mais de R$1000,00.")

print(f"Sendo o(a) {barato} o produto mais barato.")
