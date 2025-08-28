# Mundo 1 - Exercício 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# Resolvido sem auxílio.

from math import hypot

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa vai medir {hipotenusa:.2f}.")
