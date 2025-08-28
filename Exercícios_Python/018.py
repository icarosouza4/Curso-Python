# Mundo 1 - Exercício 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Resolvido com auxílio.

from math import radians, sin, cos, tan

Magenta_brilhante = "\033[95m"

print(f"{Magenta_brilhante}")

angulo = float(input("Digite o ângulo: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O ângulo de {angulo}° tem o SENO de {seno:.2f}.")
print(f"O ângulo de {angulo}° tem o COSSENO de {cosseno:.2f}.")
print(f"O ângulo de {angulo}° tem a TANGENTE de {tangente:.2f}.")
