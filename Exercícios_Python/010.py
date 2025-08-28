# Mundo 1 - Exercício 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Resolvido sem auxílio.

Vermelho_brilhante = "\033[91m"

print(f"{Vermelho_brilhante}")

dinheiro = float(input("Quanto dinheiro você tem na carteira? R$"))

dolar = dinheiro / 5.66
euro = dinheiro / 6.32

print(f"Com R${dinheiro:.2f} você pode comprar US${dolar:.2f}.")
print(f"Com R${dinheiro:.2f} você pode comprar €{euro:.2f}.")
