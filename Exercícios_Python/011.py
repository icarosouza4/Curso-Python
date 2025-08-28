# Mundo 1 - Exercício 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
# Resolvido sem auxílio.

Azul = "\033[34m"

print(f"{Azul}")

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = largura * altura
tinta = area / 2

print(f"Sua parede tem a dimensão de {(largura)}x{(altura)} e sua área é de {area}m².")
print(f"Para pintar essa parede, você precisará de {tinta}l de tinta.")
