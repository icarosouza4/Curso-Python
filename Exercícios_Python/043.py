# Mundo 2 - Exercício 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
# A) Abaixo de 18.5: Abaixo do Peso.
# B) Entre 18.5 e 25: Peso Ideal.
# C) Entre 25 até 30: Sobrepeso.
# D) Entre 30 até 40: Obesidade.
# E) Acima de 40: Obesidade Mórbida.
# Resolvido sem auxílio.

Ciano = "\033[36m"

print(f"{Ciano}")

peso = float(input("Digite o peso da pessoa: (Kg) "))
altura = float(input("Digite a altura da pessoa: (m) "))
imc = peso / (altura ** 2)

print(f"O IMC da pessoa é {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso ideal.")
elif imc < 30:
    print("Sobrepeso.")
elif imc < 40:
    print("Obesidade.")
else:
    print("Obesidade mórbida.")
