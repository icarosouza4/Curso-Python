# Mundo 1 - Exercício 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
# Resolvido sem auxílio.

Vermelho = "\033[31m"

print(f"{Vermelho}")

velocidade = float(input("Digite a velocidade do carro em km/h: "))

if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade - 80) * 7
    print(f"Você deve pagar uma multa de R$ {multa:.2f}!")
else:
    print("Você está dentro do limite de velocidade.")
