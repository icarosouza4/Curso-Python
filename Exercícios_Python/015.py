# Mundo 1 - Exercício 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# Resolvido sem auxílio.

Preto_brilhante = "\033[90m"

print(f"{Preto_brilhante}")

dia = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))

pago = (dia * 60) + (km * 0.15)

print(f"O total a pagar pelo aluguel do veículo é de R${pago:.2f}.")
