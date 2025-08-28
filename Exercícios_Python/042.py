# Mundo 2 - Exercício 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: equilátero, isósceles ou escaleno.
# Resolvido sem auxílio.

Magenta = "\033[35m"

print(f"{Magenta}")

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triângulo.")
    if r1 == r2 == r3:
        print("O triângulo é equilátero.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("As retas não podem formar um triângulo.")
