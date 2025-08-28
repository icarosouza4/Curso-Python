# Mundo 3 - Exercício 096 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
# Resolvido sem auxílio.

Branco_brilhante = "\033[97m"

print(f"{Branco_brilhante}")

def area(l,c):
    aq = l * c
    
    print(f"A área de um terreno de dimensão {l}x{c} é {aq}m².")


print(" -- Controle de terreno -- ")
print("="*27)

l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))

area(l,c)
