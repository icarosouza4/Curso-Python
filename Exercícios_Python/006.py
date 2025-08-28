# Mundo 1 - Exercício 006 - Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
# Resolvido sem auxílio.

Verde = "\033[32m"

print(f"{Verde}")

num = int(input("Digite um número: "))

print(f"O dobro de {num} é {num * 2}.")
print(f"O triplo de {num} é {num * 3}.")
print(f"A raiz quadrada de {num} é {num ** (1/2):.2f}.")
print(f"A raiz cúbica de {num} é {num ** (1/3):.2f}.")
