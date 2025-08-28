# Mundo 1 - Exercício 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Resolvido sem auxílio.

Verde = "\033[32m"

print(f"{Verde}")

preco = float(input("Digite o preço do produto:R$ "))

desconto = preco * 0.05
preco_com_desconto = preco - desconto

print(f"O preço do produto com desconto é de R${preco_com_desconto:.2f}.")
