# Mundo 1 - Exercício 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# Resolvido sem auxílio.

Magenta = "\033[35m"

print(f"{Magenta}")

medida = float(input("Uma distância em metros: "))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f"A medida de {medida}m corresponde a:")
print(f"{km}km")
print(f"{hm}hm")
print(f"{dam}dam")
print(f"{dm}dm")
print(f"{cm}cm")
print(f"{mm}mm")
