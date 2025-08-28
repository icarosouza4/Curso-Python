# Mundo 1 - Exercício 031 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
# Resolvido sem auxílio.

Branco_brilhante = "\033[97m"

print(f"{Branco_brilhante}")

distancia = float(input("Digite a distância da viagem em km: "))

print(f"Você está prestes a começar uma viagem de {distancia} km.")

if distancia <= 200:
    print(f"O preço da passagem é de R${distancia * 0.50:.2f}.")
else:
    print(f"O preço da passagem é de R${distancia * 0.45:.2f}.")
