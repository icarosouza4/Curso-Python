# Mundo 2 - Exercício 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Resolvido sem auxílio.

Amarelo = "\033[33m"

print(f"{Amarelo}")

n = int(input("Digite um número para calcular seu fatorial: "))
c = n
f = 1

while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
    
print(f)
